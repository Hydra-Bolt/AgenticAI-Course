document.getElementById('agent-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const task = document.getElementById('task').value.trim();
  const input = document.getElementById('input').value.trim();
  if (!input) return;
  document.getElementById('loading').classList.remove('hidden');
  document.getElementById('result').classList.add('hidden');
  try {
    const res = await fetch('http://localhost:8000/api/agent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task: task || 'general', input })
    });
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const data = await res.json();
    renderResult(data);
    persistLast(data);
  } catch (err) {
    console.error(err);
    alert('Error: ' + err.message);
  } finally {
    document.getElementById('loading').classList.add('hidden');
  }
});

function renderResult(data) {
  if (!data) return;
  document.getElementById('responseText').textContent = data.output || '';
  document.getElementById('metrics').innerHTML = data.metrics ? formatKV(data.metrics) : '';
  document.getElementById('safety').innerHTML = data.safety ? formatKV(data.safety) : '';
  document.getElementById('result').classList.remove('hidden');
}

function persistLast(data) {
  try {
    localStorage.setItem('lastAgentResult', JSON.stringify({ ts: Date.now(), data }));
  } catch (_) {}
}

function restoreLast() {
  try {
    const raw = localStorage.getItem('lastAgentResult');
    if (!raw) return;
    const { data } = JSON.parse(raw);
    renderResult(data);
  } catch (_) {}
}

function formatKV(obj) {
  return '<ul>' + Object.entries(obj).map(([k,v]) => `<li><strong>${k}</strong>: ${escapeHtml(JSON.stringify(v))}</li>`).join('') + '</ul>';
}

function escapeHtml(str) {
  return str.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'}[c]));
}
restoreLast();

