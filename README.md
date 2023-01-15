# KETE Smart Gardening

Dieses Repository dient als Ablage für den Code für die Semesterarbeit Smart Gardening in KETE. 

## Code
Im Ordner prototype befinden sich verschiedene Libraries die für das Betreiben der Anwendung auf einem Raspberry Pi notwendig sind.
Es ist zu beachten, dass dieser Prototyp nur mit derselben Hardware (Raspberry Pi 4 und Grove Base Kit for Raspberry Pi) funktioniert wie wir benutzt haben.
Die selbst geschriebenen Programme sind folgende:

### kete_controller_prototype_dashboard_manuell.py
Öffnet einen Flask REST-API Server der im lokalen Netz erreichbar ist. <br>
Beispielsaufruf: <br>
Aufruf: http://192.168.0.164:5000/data <br>
Payload: <br>
{
  'sensor_id': 10000,
  'sensor_name': "Sensor 1",
  'user_id': 1465214,
  'action': 'run',
};

### kete_controller_dashboard_automatic.py
Betreibt die Bewässerungsanlage automatisch. Das heisst, dass sobald der Feuchtigkeitssensor einen Wert unter 30% liefert, wird die Bewässerungsanlage für 2 Sekunden getätigt. Der Feuchtigskeitssensor misst jede Sekunde. <br>
Die Sensordaten werden an eine Firebase Realtime Database gesender, wo diese vom Dashboard konsumiert werden kann.

<br><br>



## Showcase des Prototypen
Bilder des Tests sind im Ordner media zu finden.
Das Video zum Test ist unter folgendem Link verfügbar: https://1drv.ms/v/s!AivE33WXfMsFlL13WFr03nrgVOGF0A?e=1P42fa

