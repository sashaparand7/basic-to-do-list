from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

# لود کردن فایل UI
FormClass, BaseClass = uic.loadUiType("main.ui")

class ToDoApp(QMainWindow, FormClass):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # اتصال دکمه‌ها به توابع
        self.pushButtonadd.clicked.connect(self.add_task)
        self.pushButtondelete.clicked.connect(self.remove_task)
        self.pushbuttontaskdone.clicked.connect(self.done_task)

    def add_task(self):
        task_text = self.inputtask.text()  # متن وارد شده
        if task_text:
            self.listoftasks.addItem(task_text)  # اضافه کردن به لیست
            self.inputtask.clear()               # پاک کردن LineEdit

    def remove_task(self):
        list_items = self.listoftasks.selectedItems()  # آیتم‌های انتخاب شده
        if not list_items:
            return
        for item in list_items:
            self.listoftasks.takeItem(self.listoftasks.row(item))

    def done_task(self):
        list_items =self.listoftasks.selectedItems()
        for item  in list_items:
             font = item.font()
             font.setStrikeOut(True)
             item.setFont(font)

__name__ == "__main__"
app = QApplication([])
window = ToDoApp()
window.show()
app.exec()







