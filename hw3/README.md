# Homework 3
## Abstract
* A M/M/1 Simulation
## 使用方式
* 可以透過main的變數來調整平均每次事件出現的時間以及在服務完多少個customer後結束
* 可以透過修改customer的變數來調整customer平均需要被服務的時間
## 運行架構
### Main Thread
* 產生server thread
* 產生customer並送進去該server的queue裡面
* 等待server服務結束後計算結果
### Server Thread
* 從queue中提取customer來服務
