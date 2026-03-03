function parseMember(raw = '') {
  const s = String(raw);
  const idx = s.indexOf('::');
  return idx >= 0 ? s.slice(0, idx) : s;
}

export default async function handler(req, res) {
  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!url || !token) {
    return res.status(200).json({ items: [] });
  }

  const r = await fetch(`${url}/zrevrange/leaderboard/0/9/withscores`, {
    headers: { Authorization: `Bearer ${token}` }
  });

  if (!r.ok) return res.status(500).json({ error: 'failed to fetch leaderboard' });
  const data = await r.json();
  const arr = Array.isArray(data?.result) ? data.result : [];

  const rows = [];
  for (let i = 0; i < arr.length; i += 2) {
    const member = parseMember(arr[i]);
    const score = Number(arr[i + 1] || 0);
    rows.push({ name: member, score });
  }

  return res.status(200).json({ items: rows });
}
