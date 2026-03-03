export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, score } = req.body || {};
  const cleanName = String(name || '').trim().slice(0, 16);
  const cleanScore = Number(score);

  if (!cleanName) return res.status(400).json({ error: 'name required' });
  if (!Number.isFinite(cleanScore) || cleanScore < 0) return res.status(400).json({ error: 'invalid score' });

  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!url || !token) {
    return res.status(500).json({ error: 'Leaderboard backend not configured' });
  }

  const member = `${cleanName}::${Date.now()}::${Math.random().toString(36).slice(2, 7)}`;
  const resp = await fetch(`${url}/zadd/leaderboard/${Math.floor(cleanScore)}/${encodeURIComponent(member)}`, {
    headers: { Authorization: `Bearer ${token}` }
  });

  if (!resp.ok) return res.status(500).json({ error: 'failed to save score' });
  return res.status(200).json({ ok: true });
}
