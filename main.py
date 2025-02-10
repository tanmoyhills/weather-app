import sys
import requests
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QPushButton,QWidget,QLabel, QLineEdit
from PyQt5.QtCore import Qt

class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter your city :",self)
        self.city_chatbox=QLineEdit(self)
        self.get_weather=QPushButton("Get weather",self)
        self.temperature=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description=QLabel(self)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_chatbox)
        layout.addWidget(self.get_weather)
        layout.addWidget(self.temperature)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description)

        self.setLayout(layout)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_chatbox.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_chatbox.setObjectName("city_chatbox")
        self.get_weather.setObjectName("get_weather")
        self.temperature.setObjectName("temperature")
        self.emoji_label.setObjectName("emoji_label")
        self.description.setObjectName("describtion")

        self.setStyleSheet("""
            QLabel,QPushButton{
                           font-family:calibri;}
            QLabel#city_label{
                           font-size:40px;
                           font-style:italic;
                           font-weight:bold;}
            QLineEdit#city_chatbox{
                           font-size:40px;}
            QPushButton#get_weather{
                           font-size:30px;
                           font-weight:bold}
            QLabel#temperature{
                           font-size:75px;
                           font-weight:bold;}
            QLabel#emoji_label{
                           font-size:85px;
                           font-family: segoe UI emoji;}
             QLabel#describtion{
                           font-size:45px;
                           font-family: Verdana;}
""")
        self.get_weather.clicked.connect(self.get_weathers)

    def get_weathers(self):
        api_key="e5592e419c69321e11596861730e1d5c"
        city=self.city_chatbox.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response=requests.get(url)
        data=response.json()
        if data["cod"] == 200:
             self.display_weather(data)
        else:
            self.display_error("something went wrong")
        
        
        
    def display_error(self,massage):
        self.temperature.setStyleSheet("font-size : 30px")
        self.temperature.setText(massage)
    def display_weather(self, data):
        self.temperature.setStyleSheet("font-size: 75px")
        temp=data["main"]["temp"]
        temp=temp-273.15
        self.temperature.setText(F"{temp:.0F}°C")
        weather=data["weather"][0]["description"]
        self.description.setText(weather)
        emoji = self.get_emoji_for_weather(weather)
        self.emoji_label.setText(emoji)

    def get_emoji_for_weather(self, description):
        weather_emojis = {
            "clear sky": "☀️",
            "few clouds": "🌤️",
            "scattered clouds": "⛅",
            "broken clouds": "☁️",
            "shower rain": "🌧️",
            "rain": "🌧️",
            "thunderstorm": "⛈️",
            "snow": "❄️",
            "mist": "🌫️",
        }
        return weather_emojis.get(description.lower(), "❓")


if __name__=="__main__":
    app =QApplication(sys.argv)
    win=weather_app()
    win.show()
    sys.exit(app.exec_())