# ChatGPTCEach

ChatGPTのAPIを利用してChatGPTに質問ができます。
毎回新規扱いなので連続した会話は出来ません。
 
# 実行例

質問した結果の例

![demo](https://raw.githubusercontent.com/ShiraoTakuya/ChatGPTChat/main/cap1.PNG)

# Usage

* 以下のテキストファイルを作成して内容をAPI KEYとしてください

　C:\openai_api_key.txt

* Run.cmdを実行してください
* 画面に従い問いに答えてください。それぞれ以下の意味です。

　role: ChatGPTに与える役割を入れてください(例. 優秀なプログラマ)

　ver: ChatGPTのバージョンを入れてください。

　question: ChatGPTに聞きたい内容を入れてください

会話は都度、日付の名前の.pklファイルに保存されます。

会話の内容を見たい場合はpkl_to_json.cmdを実行してください。.jsonファイルとして過去の会話が出力されます。
 
# Note
 
* OPEN AIのAPI利用料がかかります。過去の会話も毎回トークンに加算されます。十分気を付けてください。
* OPEN AI API usage fee will be charged. Past conversations are also added to the token each time. Please be careful.

# Author
  
* ShiraoTakuya
