# fastmcp-try

## 自作したMCPサーバを、Gemini Cliで使う

- Pythonの`fastmcp`を使って、簡単に、自作MCPサーバを作成
- 無料版`Gemini Cli`に自作MCPサーバを登録する
- `Gemini Cli`に話しかけると、自作MCPサーバから取得した結果を応答してくれる

> [!NOTE]
> Gemini CLI の VS Code とのより深い統合を試す  
> https://note.com/npaka/n/nd2d39c0428cc  
> 
> Gemini CLI + VS Code で Todo アプリを作成する  
> https://sight-r.sts-inc.co.jp/google_cloud_article/gemini-cli-companion-vs-code/  

## 準備（gemini-cli関連）

インストール
- nodejs
- gemini-cli

```shell
npm install -g @google/gemini-cli
```

## 準備（VSCode関連）

インストール
- VSCode
- VSCodeの拡張機能の`Gemini CLI Companion`

## geminiログイン

VSCodeのターミナルでgoogleアカウントでログイン
```shell
gemini
```

geminiステータス確認
```shell
/ide enable ※初回のみ
/ide status ※geminiとvscodeとの接続確認
/mcp list   ※MCPサーバのリスト確認
```

geminiの停止
```shell
/quit
```

## 準備（python関連）

インストール
- python
- uv

> [!NOTE]
> uvインストール  
> https://docs.astral.sh/uv/#installation  

## 準備（fastmcp関連）

> [!NOTE]
> FastMCP  
> https://github.com/jlowin/fastmcp  

セットアップ
```shell
uv init
uv venv
.venv\Scripts\activate
uv pip install fastmcp
```

## 実装、動作確認（fastmcp関連）

> [!NOTE]
> FastMCP で Streamable HTTP の MCPクライアント・サーバ の実装  
> https://note.com/npaka/n/n3e0c691fd328  
> 
> HTTPストリーミングについて調べてまとめた  
> https://note.com/kobotomomorrow/n/nf3501c361c65  

- server.py：タスク管理用のダミー機能を実装。タスクリストを取得する。
- client.py：ツール一覧呼び出し、タスクリスト取得呼び出し。

サーバ起動（`streamable-http` は `/mcp` がエンドポイント）
```shell
.venv\Scripts\activate ※ターミナル起動ごとに、一度実施が必要
python main.py
```
別ターミナルでクライアント実行
```shell
.venv\Scripts\activate ※ターミナル起動ごとに、一度実施が必要
python client.py
```

## geminiへのMCP登録

> [!NOTE]
> Gemini CLIでMCPを使ってみた  
> https://qiita.com/n0bisuke/items/8686a74d8edcb5d29265  

以下のファイルに、作成したMCPサーバを登録する
`C:\Users\ユーザ名\.gemini\settings.json`
```json
{

  ～～～ : {
  },
  "mcpServers": {
    "MyTeamTaskManagementServer": {
      "httpUrl": "http://localhost:8000/mcp"
    }
  }
}
```

## geminiの動作確認

VSCodeのターミナルでログイン
```shell
gemini
```

```shell
> /mcp

Configured MCP servers:
 MyTeamTaskManagementServer - Ready (4 tools)
  Tools:
  - getAllTaskList
  - getCompleteTaskList
  - getUnCompleteTaskList
  - getUserIdList
```

```shell
> 私のチームのメンバーを教えて

✦ チームのメンバーは次のとおりです。
   * suzuki
   * tanaka
   * yamada
```

```shell
> suzukiの全てのタスクを教えて

✦ suzukiさんの全てのタスクは次のとおりです。
   * Task 1
   * Task 2
   * Task 3
```

geminiの停止
```shell
/quit
```

## 参考

> [!NOTE]
> MCP（Model Context Protocol）の最小動作サンプル  
> https://zenn.dev/ted99/articles/8e679ad20f4f48  
>
> API GatewayとLambdaでリモートMCPサーバーができた！  
> GitHub Copilot Chatをエージェントモードにし、「calculateツールを使って、 2足す3を実行して」と質問  
> https://qiita.com/moritalous/items/146095294ec13ae9f9b5#vscode%E3%81%8B%E3%82%89%E6%8E%A5%E7%B6%9A%E7%A2%BA%E8%AA%8D  

