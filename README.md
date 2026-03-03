# 3D Shooting Range (Web)

網頁 3D 小遊戲（Three.js）：第一人稱射擊靶場。

## 操作
- `W A S D`：移動
- `Space`：跳躍
- 滑鼠：視角
- 左鍵：射擊
- 右鍵：瞄準（倍鏡）
- `ESC`：暫停選單

## 排行榜（後端）
本專案使用 Vercel API Route + Upstash Redis：
- `GET /api/leaderboard`
- `POST /api/score`

請在 Vercel 專案設定環境變數：
- `UPSTASH_REDIS_REST_URL`
- `UPSTASH_REDIS_REST_TOKEN`

未設定時，前端仍可遊玩，但排行榜不會儲存。

## 部署到 Vercel
1. Push 到 GitHub
2. 在 Vercel 匯入 `Chihen-Tai/opencode-snake`
3. Framework: `Other`
4. Build Command 留空
5. Output Directory 留空
6. 設定上方兩個環境變數（若要排行榜）
7. Deploy
