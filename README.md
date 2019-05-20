# SQL Detector

SQLを生成するロジックを書いているプロダクションチームに贈る―― SQL 比較ツールに全米が涙

## 使用方法
1. config ファイルを作成する。
    ```bash
      python create_configure.py -f FILE -m METHOD -o OUTPUT
    ```
    - FILE: Detect 対象のファイルパス（ex: path.to.module）※必須
    - METHOD: Detect 対象のメソッド名（正規表現）
    - OUTPUT: config ファイルのファイル名（なければ config_{timestamp} の形式で出力）
    
1. config ファイルを基に sql を書き出す。
    ```bash
      python create_sql_file.py -c CONFIG -m MOCK
    ```
    - CONFIG: 1で作成した config ファイル名（config ディレクトリのファイルを指定してください）※必須
    - MOCK: 対象ファイル内の関数の実行中に Mock する必要のあるメソッド（DB にアクセスするメソッドなど）
   
   作成されたファイルは output ディレクトリに格納されます。

1. output ディレクトリ内のファイルから2つピックアップして差分を検出する。
    ```bash
      python diff_checker.py -f1 FILE1 -f2 FILE2
    ```
    - FILE1: 差分を検出したいファイル名（output ディレクトリのファイルを指定してください）
    - FILE2: 差分を検出したいファイル名（output ディレクトリのファイルを指定してください）

`python create_sql_file.py -c config_20190513214459 -m dbc.execute`