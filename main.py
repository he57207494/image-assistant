import os

from PIL import ImageFont, ImageDraw, ImageEnhance, Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics, QFontInfo
from PyQt5.QtWidgets import QMessageBox, QFontDialog, QFileDialog

from ui import main_ui
from ui import waterMarkWindow
from ui import renameWindow

class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.setupUi(self)
        self.open_watermark_button.clicked.connect(self.open_watermark)
        self.open_rename_button.clicked.connect(self.open_rename)

    def open_watermark(self):
        self.waterMarkWindow = waterMarkWindow.Ui_waterMarkWindow()
        self.waterMarkWindow.setFixedSize(665,500)
        self.waterMarkWindow.statusbar.showMessage("准备就绪....")

        self.waterMarkWindow.button_loadImage.clicked.connect(self.getFiles)
        self.waterMarkWindow.listWidget.itemClicked.connect(self.itemClick)
        self.waterMarkWindow.btn_fontSet.clicked.connect(self.setFont)
        self.waterMarkWindow.btn_brower.clicked.connect(self.setImg)
        self.waterMarkWindow.btn_brower2.clicked.connect(self.selectSave)
        self.waterMarkWindow.btn_execute.clicked.connect(self.execute)

        self.waterMarkWindow.comboBox.addItems(["左上角", "右上角", "左下角", "右下角", "中间"])
        self.waterMarkWindow.comboBox.setCurrentIndex(4)

        icon = QtGui.QIcon()

        self.waterMarkWindow.show()

    def open_rename(self):
        self.renameWindow = renameWindow.Ui_renameWindow()
        self.renameWindow.setFixedSize(473, 467)
        self.renameWindow.statusbar.showMessage("准备就绪....")

        self.renameWindow.pushButton.clicked.connect(self.getFiles_rename)
        self.renameWindow.pushButton_2.clicked.connect(self.reName)

        self.renameWindow.tableWidget.setColumnWidth(0,100)
        self.renameWindow.tableWidget.setColumnWidth(1,250)

        self.renameWindow.show()

    # 获取文件夹下的图片
    def getFiles(self):
        try:
            self.img_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", os.getcwd())
            self.list = os.listdir(self.img_path)

            num = 0
            self.waterMarkWindow.listWidget.clear()
            for i in range(len(self.list)):
                filepath = os.path.join(self.img_path, self.list[i])
                filetype = os.path.splitext(filepath)[1]
                if os.path.isfile(filepath) and filetype in ['.jpg', '.png', '.jpeg', '.bmp']:
                    num += 1
                    self.waterMarkWindow.listWidget.addItem(self.list[i])
            self.waterMarkWindow.statusbar.showMessage("共有%d张图片" % num)
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))

    # 点击图片列表,预览图片
    def itemClick(self, item):
        os.startfile(self.img_path + '/' + item.text())

    # 设置字体
    def setFont(self):
        self.waterfont,ok = QFontDialog.getFont()
        if ok:
            self.waterMarkWindow.ledit_text.setFont(self.waterfont)
            self.fontsize = QFontMetrics(self.waterfont)
            self.fontInfo = QFontInfo(self.waterfont)

    def setImg(self):
        try:
            self.waterimg = QFileDialog.getOpenFileName(None, "选取文件",self.img_path, "Image Files(*.jpg *.png *.jpeg *.bmp)")
            self.waterMarkWindow.ledit_addImage.setText(self.waterimg[0])
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))

    def selectSave(self):
        try:
            self.save_path = QFileDialog.getExistingDirectory(None, "选取文件夹", os.getcwd())
            self.waterMarkWindow.ledit_savePostion.setText(self.save_path)
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))

    def textMark(self,img,newImagePath):
            print(img,newImagePath)
        # try:
            im = Image.open(img).convert('RGBA')
            newImg = Image.new('RGBA', im.size, (255, 255, 255, 0))
            font = ImageFont.truetype("./font/simhei.ttf", self.fontsize.height())
            imagedraw = ImageDraw.Draw(newImg)
            imgwidth,imgheight = im.size
            txtwidth = self.fontsize.maxWidth()
            txtheight = self.fontsize.height()
            if self.waterMarkWindow.comboBox.currentIndex() == 0:
                positon = (0, 0)
            elif self.waterMarkWindow.comboBox.currentIndex() == 1:
                positon = (imgwidth - txtwidth, 0)
            elif self.waterMarkWindow.comboBox.currentIndex() == 2:
                positon = (0, imgheight - txtheight)
            elif self.waterMarkWindow.comboBox.currentIndex() == 3:
                positon = (imgwidth - txtwidth, imgheight - txtheight)
            elif self.waterMarkWindow.comboBox.currentIndex() == 4:
                positon = ((imgwidth - txtwidth)/2, (imgheight - txtheight)/2)

            # 添加文字水印
            imagedraw.text(positon, self.waterMarkWindow.ledit_text.text(), font=font, fill=(0, 0, 0, 128))

            #
            alpha = newImg.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(int(self.waterMarkWindow.horizontalSlider.value())/10.0)
            newImg.putalpha(alpha)

            Image.alpha_composite(im, newImg).save(newImagePath)
        # except Exception as e:
        #     QMessageBox.critical(self, "错误", str(e))

    def imgMark(self,img,newImagePath):
        # try:
            im = Image.open(img).convert('RGBA')
            mark = Image.open(self.waterMarkWindow.ledit_savePostion).convert('RGBA')
            imgwidth, imgheight = im.size
            markwidth, markheight = mark.size

            # 计算水印大小
            scale = 10
            markscale = max(imgwidth / (scale * markwidth), imgheight / (scale * markheight))
            newsize = (int(markwidth * markscale), int(markheight * markscale))

            rgbamark = mark.resize(newsize, Image.ANTIALIAS)
            markwidth, markheight = rgbamark.size

            # 计算水印位置
            if self.waterMarkWindow.comboBox.currentIndex() == 0:
                positon = (0, 0)
            elif self.waterMarkWindow.comboBox.currentIndex() == 1:
                positon = (imgwidth - markwidth, 0)
            elif self.waterMarkWindow.comboBox.currentIndex() == 2:
                positon = (0, imgheight - markheight)
            elif self.waterMarkWindow.comboBox.currentIndex() == 3:
                positon = (imgwidth - markwidth, imgheight - markheight)
            elif self.waterMarkWindow.comboBox.currentIndex() == 4:
                positon = ((imgwidth - markwidth)/2, (imgheight - markheight)/2)

            rgbmarkapha = rgbamark.convert('L').point(lambda i:i/int(self.waterMarkWindow.horizontalSlider.value()))
            rgbamark.putalpha(rgbmarkapha)
            im.paste(rgbamark, positon, rgbmarkapha)
            im.save(newImagePath)
        # except Exception as e:
        #     QMessageBox.critical(self, "错误", str(e))

    def execute(self):
        try:
            if self.waterMarkWindow.ledit_savePostion.text() == "":
                QMessageBox.critical(self, "错误", "请选择保存位置")
                return
            else:
                num = 0
                for i in range(len(self.list)):
                    filetype = os.path.splitext(self.list[i])[1]
                    if filetype not in ['.jpg', '.png', '.jpeg', '.bmp']:
                        continue
                    if self.waterMarkWindow.rbtn_addText.isChecked():
                        if self.waterMarkWindow.ledit_text.text() == "":
                            QMessageBox.critical(self, "错误", "请输入水印文字")
                            return
                        else:
                            self.textMark(self.img_path + '/' + self.list[i], self.save_path + '/' + self.list[i])
                    elif self.waterMarkWindow.rbtn_addImage.isChecked():
                        if self.waterMarkWindow.ledit_addImage.text() == "":
                            QMessageBox.critical(self, "错误", "请选择水印图片")
                            return
                        else:
                            self.imgMark(self.img_path + '/' + self.list[i], self.save_path + '/' + self.list[i])
                    num += 1
                self.waterMarkWindow.statusbar.showMessage("共处理%d张图片" % num)
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))


    #===========================以下用于处理批量重命名============================================
    def getFiles_rename(self):
        try:
            self.img_path = QFileDialog.getExistingDirectory(None, "选取文件夹", os.getcwd())
            self.renameWindow.lineEdit_5.setText(self.img_path)
            self.list = os.listdir(self.img_path)

            print(self.img_path)
            print(self.list)

            num = 0
            self.renameWindow.tableWidget.clearContents()
            self.renameWindow.tableWidget.setRowCount(0)
            for i in range(0,len(self.list)):
                filepath = os.path.join(self.img_path,self.list[i])
                if os.path.isfile(filepath):
                    imgType = os.path.splitext(filepath)[1] #获取扩展名
                    if imgType in  ['.jpg', '.jpeg', '.png']:
                        self.renameWindow.tableWidget.insertRow(num)
                        self.renameWindow.tableWidget.setItem(num,0,QtWidgets.QTableWidgetItem(self.list[i]))
                        self.renameWindow.tableWidget.setItem(num,1,QtWidgets.QTableWidgetItem(self.img_path))
                        num += 1
                        print(num,self.list[i],self.img_path)
            self.renameWindow.statusbar.showMessage("共有"+str(num)+"张")
            self.rename_image_num = num
            print(self.rename_image_num)

        except Exception:
            QMessageBox.warning(None,"警告","请选择一个有效路径.....",QMessageBox.Ok)

    def reName(self):
        num = 0
        filename = ""
        newfilename = ""
        try:
            for i in range(0,len(self.list)):
                filepath = os.path.join(self.img_path,self.list[i])
                if os.path.isfile(filepath):
                    imgType = os.path.splitext(filepath)[1]  # 获取扩展名
                    if imgType in ['.jpg', '.jpeg', '.png']:
                        if self.renameWindow.radioButton.isChecked():   #文件名大写
                            newfilename = str(self.list[i]).upper()
                            newfilpath = os.path.join(self.img_path,newfilename)
                            os.rename(filepath,newfilpath)
                        elif self.renameWindow.radioButton_2.isChecked():
                            newfilename = str(self.list[i]).lower()
                            newfilpath = os.path.join(self.img_path,newfilename)
                            os.rename(filepath,newfilpath)
                        elif self.renameWindow.radioButton_3.isChecked():
                            strid = self.renameWindow.lineEdit_3.text()
                            id = int(self.renameWindow.lineEdit.text())
                            step = int(self.renameWindow.lineEdit_2.text())
                            template = "{:0>3}"
                            newfilename = strid+ template.format(id+step*num)+imgType
                            newfilepath = os.path.join(self.img_path,newfilename)
                            os.rename(filepath,newfilepath)

                        self.renameWindow.tableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(newfilename))
                        num += 1
                self.renameWindow.statusbar.showMessage("批量命名完成，一共处理图片"+str(num)+"张")
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())