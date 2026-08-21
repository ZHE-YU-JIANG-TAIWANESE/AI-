# Open Character Workbench（OCW）

OCW 是一套給 **AI／人類共同操作 Blender 角色建模** 的開源工作台。它不是一鍵把圖片變 3D 的黑箱模型，而是把真正需要的工作環境整理成可重現流程：

> 參考圖 → 隔離工作室 → Blender 建模 → 可檢查交件 → 再迭代

目前 v0.1.0 提供：

- `ocw doctor`：檢查 Blender 工作站。
- `ocw new-job`：建立任務 manifest，保存時間戳與參考圖 SHA-256。
- `ocw stage`：只把宣告過的證據送進乾淨工作室。
- `ocw validate`：檢查 `.blend`、正面、側面、3/4 預覽與 handoff 是否齊全。
- vendor-neutral agent contract：Gemini、Codex、Claude、local model 或人類都可以接同一套工作台。
- synthetic 正／側參考範例，不需要公開私人角色素材也能測試。

## 快速開始

```bash
python -m pip install -e .
ocw doctor

ocw new-job \
  --front /path/to/front.png \
  --side /path/to/side.png \
  --output jobs/my-character.json

ocw stage \
  --job jobs/my-character.json \
  --studio .ocw/studios/my-character
```

建模完成後：

```bash
ocw validate --delivery .ocw/studios/my-character/vendor-output
```

這個專案的核心觀念是：**AI 可以換，工作室不必跟著換。** 同一個 reference、同一個 job contract、同一個交件規格，可以公平比較不同 agent、不同工具與不同建模方法。

程式與文件採 Apache-2.0；使用者自行提供的美術、模型與參考資料不會因使用 OCW 而被重新授權。
