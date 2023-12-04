import os
import imutils
import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


class RegistroEMP:
    def __init__(self, view, data_emp):
        self.root = view
        self.cap = None
        self.tomar = None
        self.data = data_emp
        self.prototxt = "Modelos/deploy.prototxt"
        self.model = "Modelos/res10_300x300_ssd_iter_140000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(self.prototxt, self.model)
        self.OutFolderPathUser = 'Data/Users'
        self.PathUserCheck = 'Data/Users/'
        self.OutFolderPathFace = 'Data/Face'
        self.root.state('zoomed')
        self.root.title("Registro facial de Empleados")
        self.root.iconbitmap("icono.ico")
        self.root.resizable(False, False)

        self.frame_video = Frame(self.root, bg="lightblue")
        self.frame_video.pack(side="top", fill="both", expand=True)

        self.frame_opciones = Frame(self.root, bg="lightblue")
        self.frame_opciones.pack(side="bottom", fill="both", expand=True)

        self.label_count = Label(self.frame_opciones)
        self.label_count.pack(padx=20, pady=20)

        self.label_video = Label(self.frame_video)
        self.label_video.place(rely=0.5, relx=0.5, anchor="center")

        self.btn_empezar = Button(self.frame_opciones, text="Empezar video", command=self.iniciarVideo)
        self.btn_empezar.pack(side=LEFT, padx=50, pady=10)
        self.btnCapturarFoto = Button(self.frame_opciones, text="Capturar rostro")
        self.btnCapturarFoto.pack(side=LEFT, padx=50, pady=10)
        self.btn_lista = Button(self.frame_opciones, text="Parar video")
        self.btn_lista.pack(side=LEFT, padx=50, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.cap.release()
        self.root.destroy()

    def iniciarVideo(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        contador = 0
        while True:
            ret, frame = self.cap.read()
            if ret is False:
                break
            # frameCopy = frame.copy()
            # frameCopy = cv2.flip(frameCopy, 1)
            # frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2RGB)
            # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_gray = cv2.flip(frame, 1)
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            frame_resized = cv2.resize(frame, (300, 300))

            # Create a blob
            blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104, 117, 123))

            self.net.setInput(blob)
            detections = self.net.forward()

            for detection in detections[0][0]:
                if detection[2] > 0.9:
                    self.btnCapturarFoto.config(state="active")
                    box = detection[3:7] * [width, height, width, height]
                    x_start, y_start, x_end, y_end = int(box[0]), int(box[1]), int(box[2]), int(box[3])
                    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
                    cv2.putText(frame, "Conf: {:.2f}".format(detection[2] * 100), (x_start, y_start - 5), 1, 1.2,
                                (0, 255, 255),
                                2)
                    if self.tomar:
                        cv2.putText(frame, "Contador: {}".format(contador), (x_start, y_end + 30), 1,
                                    1.2,
                                    (0, 255, 255),
                                    2)
                        face_image = frame_gray[y_start:y_end, x_start:x_end]
                        cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (255, 255, 0), 2)
                        face_image = cv2.resize(face_image, (150, 150), interpolation=cv2.INTER_CUBIC)
                        image_path = os.path.join(self.OutFolderPathFace, f'{self.data[1]}_{contador}.png')
                        cv2.imwrite(image_path, face_image)
                        contador += 1

            # cv2.imshow("Frame", frame)
            frame = imutils.resize(frame, width=1280)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            self.label_video.configure(image=img)
            self.label_video.image = img
            self.root.update()
        self.cap.release()


if __name__ == "__main__":
    panel = Tk()
    empleado = [2, "Adolfo", "Santa lucia", "A"]
    app = RegistroEMP(panel, empleado)
    panel.mainloop()
