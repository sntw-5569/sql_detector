# SQL Detector

SQLを生成するロジックを書いているプロダクションチームに贈る―― SQL 比較ツールに全米が涙

## 必須
- Python 3.6 ~
- Git

## 使用方法  
### 準備  
1. config ファイルを作成する。
    ```bash
      python create_configure.py -f FILE -m METHOD -o OUTPUT
    ```
    - FILE: Detect 対象のファイルパス（ex: path.to.module）※必須
    - METHOD: Detect 対象のメソッド名（正規表現）
    - OUTPUT: config ファイルのファイル名（なければ config_{timestamp} の形式で出力）
    
2. config ファイルを基に sql を書き出す。
    ```bash
      python create_sql_file.py -c CONFIG -m MOCK
    ```
    - CONFIG: 1で作成した config ファイル名（config ディレクトリのファイルを指定してください）※必須
    - MOCK: 対象ファイル内の関数の実行中に Mock する必要のあるメソッド（DB にアクセスするメソッドなど）
   
   作成されたファイルは output ディレクトリに格納されます。

3. output ディレクトリ内のファイルから2つピックアップして差分を検出する。
    ```bash
      python diff_checker.py -f1 FILE1 -f2 FILE2
    ```
    - FILE1: 差分を検出したいファイル名（output ディレクトリのファイルを指定してください）
    - FILE2: 差分を検出したいファイル名（output ディレクトリのファイルを指定してください）

### サンプル動作方法  
1. python3.6以上をインストール
2. Gitのインストール
3. このREADMEファイルと同階層のディレクトリで以降を実施
4. python仮想環境を作成
      ```bash
      python3 -m venv .sqldect
      ```
      - インストール状態に合わせてpython3やpython36、ただのpythonなど適宜お使いの環境に合わせてください。
5. venv を起動
  - macOS、Linuxは下記コマンド
    ```bash
    source .sqldect/bin/activate
    ```
  - Windowsは下記コマンド 
    ```bash
    .sqldect/bin/activate.bat
    ```
6. 必要なパッケージのインストール
     ```bash
     pip install -r py_git/requriments.txt
     ```
     - Windowsは`/`を`¥`にする
7. インストール後下記のコマンドを実行
   ```bash
   python sample_run_dtct.py dummy_first dummy_second
   ```
8. ライン入力でコンフィグファイルの相対パスを入力
    ```bash
    sql_detector/config/config_20190513214459
    ```
9.  ライン入力でパッチするメソッドを指定
    ```bash
    dbc.execute
    ```
10. 比較結果の出力が表示される（sql_detector/outputの出力結果と差異を表示している）
