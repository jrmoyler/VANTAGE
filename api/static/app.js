const generateBtn = document.getElementById('generate-btn');
const askBtn = document.getElementById('ask-btn');
const intentInput = document.getElementById('intent');
const queryInput = document.getElementById('query');
const generateOutput = document.getElementById('generate-output');
const askOutput = document.getElementById('ask-output');

const renderList = (id, items) => {
  const root = document.getElementById(id);
  root.innerHTML = '';
  items.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item;
    root.appendChild(li);
  });
};

const loadStaticData = async () => {
  const [styles, principles, knowledge] = await Promise.all([
    fetch('/api/styles').then((r) => r.json()),
    fetch('/api/principles').then((r) => r.json()),
    fetch('/api/knowledge').then((r) => r.json()),
  ]);

  renderList('styles-output', styles.styles.slice(0, 12));
  renderList('principles-output', principles.principles.slice(0, 12).map((p) => `${p.name}: ${p.summary}`));
  renderList('knowledge-output', knowledge.domains.map((d) => `${d.title} (${d.count})`));
};

generateBtn.addEventListener('click', async () => {
  const intent = intentInput.value.trim();
  if (!intent) {
    generateOutput.textContent = 'Please provide a build intent.';
    return;
  }

  generateBtn.disabled = true;
  try {
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ intent }),
    });

    if (!res.ok) {
      generateOutput.textContent = `Failed (${res.status})`;
      return;
    }

    const data = await res.json();
    generateOutput.textContent = [
      '# COMPONENTS',
      ...data.components.map((c) => `- ${c}`),
      '',
      '# PRINCIPLES',
      ...data.principles.map(([name, why]) => `- ${name}: ${why}`),
      '',
      '# STRUCTURED PROMPT',
      data.structured_prompt,
    ].join('\n');
  } finally {
    generateBtn.disabled = false;
  }
});

askBtn.addEventListener('click', async () => {
  const query = queryInput.value.trim();
  if (!query) {
    askOutput.innerHTML = '<li>Please provide a search query.</li>';
    return;
  }

  askBtn.disabled = true;
  try {
    const res = await fetch('/api/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();
    askOutput.innerHTML = '';

    if (!data.results.length) {
      askOutput.innerHTML = '<li>No direct results found.</li>';
      return;
    }

    data.results.slice(0, 8).forEach((item) => {
      const li = document.createElement('li');
      li.textContent = `${item.domain}: ${JSON.stringify(item.record)}`;
      askOutput.appendChild(li);
    });
  } finally {
    askBtn.disabled = false;
  }
});

loadStaticData().catch(() => {
  document.getElementById('status-pill').textContent = 'API: degraded';
});
