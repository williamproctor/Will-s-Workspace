/* ============================================
   POSITIONING ASSESSMENT QUIZ — LOGIC
   ============================================
   All quiz content, scoring rules, and UI state
   are managed here. Edit question text or outcome
   write-ups without touching the logic below.
   ============================================ */

// ──────────────────────────────────────────────
// CONFIGURATION
// ──────────────────────────────────────────────

/*
 * EMAIL ENDPOINT CONFIGURATION
 * ────────────────────────────
 * Set this to your email service's form endpoint.
 * When null, the form will store the email in
 * localStorage and proceed to results (dev mode).
 *
 * Examples:
 *   ConvertKit:  'https://app.convertkit.com/forms/YOUR_FORM_ID/subscriptions'
 *   Mailchimp:   'https://YOUR_DOMAIN.us1.list-manage.com/subscribe/post?u=XXXXX&id=YYYYY'
 *   HubSpot:     'https://api.hsforms.com/submissions/v3/integration/submit/PORTAL_ID/FORM_ID'
 *   Formspree:   'https://formspree.io/f/YOUR_FORM_ID'
 *   Custom:      'https://your-api.com/subscribe'
 *
 * The form sends: { name: '...', email: '...' }
 */
const EMAIL_ENDPOINT = null;

// ──────────────────────────────────────────────
// QUESTION DATA
// ──────────────────────────────────────────────

const QUESTIONS = [
  {
    id: 1,
    text: "Does your product reliably spread user-to-user without marketing forcing it? (viral loops, network effects, sharing)",
    yesContext: "You have a realistic path to Platform Play because distribution can come from usage, not just campaigns. Lower marginal cost per new use case because users do the work.",
    noContext: "You do not get the Notion exception. You must earn reach through content, paid, partners, or sales. Relevance beats breadth — this pushes you toward Focused Wedge."
  },
  {
    id: 2,
    text: "Can you credibly tell one story that is true for most of the buyers you want right now?",
    yesContext: "You can run a single narrative and repeat yourself 1,000 ways without it breaking. One POV, many derivatives across channels. Easier message discipline and AI search authority.",
    noContext: "You're trying to force one story onto multiple buyer situations. That's how teams drift into hedged positioning. You'll need 2–4 distinct narratives tied to real use cases."
  },
  {
    id: 3,
    text: "Is there a clear, entrenched category leader buyers default to today?",
    yesContext: "You are in April Dunford's Head-to-Head world if you go broad. Buyers already have a mental shortlist. You need crisp competitive differentiation and repeated proof.",
    noContext: "There's a chance to shape the game. Education and definition content can work because buyers aren't anchored. Thought leadership can create demand."
  },
  {
    id: 4,
    text: "Do buyers already have an established name for what you do? (category maturity)",
    yesContext: "Category creation is less likely to be the right move. You're operating in an existing market structure. \"Best for X\" proof works well.",
    noContext: "This is the set-up for Create New Game — but only a minority should attempt it. You must educate, name, and defend the problem and the category."
  },
  {
    id: 5,
    text: "Do you have one specific use case where you win disproportionately often vs alternatives?",
    yesContext: "You have the raw material for April's Big Fish, Small Pond approach. Use-case assets like playbooks, ROI comparisons, and case studies become your core engine.",
    noContext: "If you can't point to a reliable wedge, segmentation becomes guesswork and the org drifts into sprawl. You'll end up making a little content for everyone."
  },
  {
    id: 6,
    text: "Can you afford 12+ months of consistent, high-volume marketing without needing immediate pipeline proof?",
    yesContext: "You can sustain the repetition tax of Head-to-Head or the education tax of Create New Game. Ongoing output across channels, not one hero launch.",
    noContext: "You need a faster learning loop and clearer conversion path. High-intent use-case content beats broad category thought leadership."
  },
  {
    id: 7,
    text: "Do you have enough team capacity to support your positioning without volume sprawl?",
    yesContext: "You can execute Head-to-Head repetition, segmented campaigns with governance, or category education. Multiple formats, consistent cadence.",
    noContext: "Broad positioning is dangerous. You will be forced into \"one more asset, one more audience\" requests. Pick one story, one ICP, one use case."
  },
  {
    id: 8,
    text: "Do your best channels reward message consistency over coverage? (AI search, authority, organic social)",
    yesContext: "One narrative compounded over time is a competitive advantage. Repeat the same language across platforms. Message governance matters.",
    noContext: "You win by being extremely relevant to a specific situation, not broadly consistent. Segment landing pages, webinars, use-case proof."
  },
  {
    id: 9,
    text: "Do customers discover you primarily through a specific workflow/problem moment (not a broad category search)?",
    yesContext: "Use-case positioning is naturally aligned to how buyers find and choose. \"How to solve X\" content, templates, and proof will be your primary engine.",
    noContext: "Buyers may be shopping by category and comparing alternatives broadly. Category narrative and competitive positioning become more important."
  },
  {
    id: 10,
    text: "Is your product fundamentally horizontal (many teams can use it) rather than a single workflow tool?",
    yesContext: "You can be a platform if distribution mechanics exist. Platform narrative plus enablement for many use cases. But you need governance so \"horizontal\" doesn't become \"incoherent.\"",
    noContext: "You are closer to a wedge by nature. Trying to speak to everyone will feel like a compromise. Go deep on the workflow and outcomes."
  },
  {
    id: 11,
    text: "Are you willing (and able) to educate the market on a new problem/category for 12–24 months?",
    yesContext: "You may fit April Dunford's Create a New Game path — but only if you can sustain consistency and output. Category definition, POV, objections, and proof that the category deserves to exist.",
    noContext: "Don't attempt category creation. It will look like confusion. Anchor in an existing category or a narrow use case."
  },
  {
    id: 12,
    text: "Can leadership tolerate saying \"no\" to most of the TAM for 6–12 months?",
    yesContext: "You can commit to a wedge without political whiplash. One ICP, one core use case, repeated. You avoid hedged positioning.",
    noContext: "You will get pulled into \"cover the TAM.\" That either requires Category-Leader resources or strict governance to avoid sprawl."
  }
];

// ──────────────────────────────────────────────
// OUTCOME DATA
// ──────────────────────────────────────────────

const OUTCOMES = {
  "head-to-head": {
    slug: "head-to-head",
    title: "Head-to-Head (Category Leader)",
    subtitle: "You compete directly in an existing category against the default leaders. This is April Dunford's Head-to-Head style.",
    whoFor: [
      "Established company or well-funded challenger",
      "Strong team capacity to execute consistent repetition across channels",
      "Leadership alignment on one story and one market definition"
    ],
    whySense: "Buyers already understand the category, so your job is to become the best-known, most trusted, most repeated option.",
    gtmRequirements: [
      "High repetition: one narrative expressed across website, sales, social, and events",
      "Competitive proof: comparisons, case studies, objections, enablement",
      "Event presence that matches the category (industry conferences, flagship sponsorships)"
    ],
    gains: [
      "Bigger TAM and category-level brand",
      "Faster scaling once you win mindshare"
    ],
    losses: [
      "Focus — you will trade specificity for breadth",
      "You accept a higher repetition tax (and higher spend)"
    ],
    examples: "Salesforce (incumbent dynamic), Slack (broad category narrative once established).",
    redFlags: [
      "You try to go broad with a small team",
      "Messaging shifts quarterly",
      "You don't have a distribution advantage and you can't out-produce/out-spend"
    ],
    workshopNote: "This is where \"repeat yourself 1,000 ways\" matters most — and where hedging creates volume sprawl."
  },

  "focused-wedge": {
    slug: "focused-wedge",
    title: "Big Fish, Small Pond (Focused Wedge)",
    subtitle: "You dominate a subsegment of an existing market by being the best for a specific use case. This is April Dunford's Big Fish, Small Pond.",
    whoFor: [
      "Early-stage or resource-constrained teams",
      "Companies with a clear use case where win rates are already strong",
      "Enterprise motions where proof and relevance beat broad claims"
    ],
    whySense: "Focus lets you build proof, earn distribution in a niche, and avoid content sprawl.",
    gtmRequirements: [
      "1 primary ICP + 1 primary use case narrative",
      "Use-case asset stack: landing page, ROI story, 3–5 strong case studies, objection handling",
      "Targeted events: webinars, partner co-marketing, field dinners in the niche"
    ],
    gains: [
      "Clarity, conversion, faster learning",
      "Lower content burden"
    ],
    losses: [
      "You say \"no\" to big parts of the TAM",
      "You may look \"small\" until you expand"
    ],
    examples: "Superhuman (highly specific early story), many B2B winners who start as \"best for X.\"",
    redFlags: [
      "Leadership refuses to focus",
      "You pick a wedge that is not actually winnable",
      "You expand segments before proof exists"
    ],
    workshopNote: "This is the antidote to hedged positioning. It prevents volume sprawl."
  },

  "platform-play": {
    slug: "platform-play",
    title: "Platform Play (The Notion Model)",
    subtitle: "A horizontal platform with viral mechanics that can support many micro-positionings because users and community propagate use cases.",
    whoFor: [
      "Horizontal products with strong sharing loops",
      "Products where users create artifacts that naturally recruit other users",
      "Companies able to enable a community ecosystem (templates, education, creators)"
    ],
    whySense: "You do not have to staff every micro-campaign because usage itself becomes distribution.",
    gtmRequirements: [
      "One platform narrative, repeated consistently",
      "Heavy enablement: templates, tutorials, community programs",
      "Lifecycle and product marketing tightly integrated"
    ],
    gains: [
      "Breadth without proportional marketing headcount",
      "Many entry points into adoption"
    ],
    losses: [
      "If mechanics weaken, the whole model breaks",
      "Requires discipline so \"platform\" doesn't become vague"
    ],
    examples: "Notion, and to a degree Slack (viral/team adoption dynamics).",
    redFlags: [
      "No true viral loop",
      "You try to run thousands of micro-positionings as a company-driven campaign plan",
      "Messaging becomes inconsistent across channels (hurts AI search authority)"
    ],
    workshopNote: "This is explicitly positioned as the exception most companies shouldn't copy."
  },

  "create-new-game": {
    slug: "create-new-game",
    title: "Create New Game (Category Creator)",
    subtitle: "You create and win a new category by teaching the market a new way to think. April Dunford cautions that only ~10% should attempt it.",
    whoFor: [
      "Companies with enough runway and output capacity to educate for 12–24 months",
      "Products that truly don't fit existing buyer categories",
      "Teams with strong POV, founder/executive conviction, and message discipline"
    ],
    whySense: "If buyers cannot place you, competing head-to-head can be impossible. Creating a new frame can unlock demand.",
    gtmRequirements: [
      "Category education engine: definitions, objections, proof, language standardization",
      "Flagship educational moments: workshops, research, \"state of\" reports",
      "Tight consistency across channels to build authority"
    ],
    gains: [
      "You stop being compared to the wrong alternatives",
      "You can become the default for the new frame"
    ],
    losses: [
      "Time — category creation is slow",
      "A high burden of explanation"
    ],
    examples: "Modern category creators vary by era; use this pattern cautiously. Most companies should not attempt.",
    redFlags: [
      "You don't have enough runway",
      "Your POV is not distinct",
      "You cannot sustain the output"
    ],
    workshopNote: "This is the hardest path and amplifies the cost of inconsistency."
  }
};

// ──────────────────────────────────────────────
// STATE
// ──────────────────────────────────────────────

let currentQuestion = 0;   // 0-indexed
let answers = [];           // array of booleans (true = YES)
let contextOpen = false;

// ──────────────────────────────────────────────
// DOM REFERENCES
// ──────────────────────────────────────────────

const $intro      = document.getElementById('intro');
const $quiz       = document.getElementById('quiz');
const $emailGate  = document.getElementById('email-gate');
const $results    = document.getElementById('results');

const $startBtn   = document.getElementById('start-btn');
const $backBtn    = document.getElementById('back-btn');
const $btnYes     = document.getElementById('btn-yes');
const $btnNo      = document.getElementById('btn-no');
const $progressBar = document.getElementById('progress-bar');
const $counter    = document.getElementById('question-counter');
const $questionText = document.getElementById('question-text');
const $toggleCtx  = document.getElementById('toggle-context');
const $ctxBody    = document.getElementById('context-body');
const $ctxYes     = document.getElementById('context-yes-text');
const $ctxNo      = document.getElementById('context-no-text');

const $emailForm  = document.getElementById('email-form');
const $retakeBtn  = document.getElementById('retake-btn');

// ──────────────────────────────────────────────
// SCREEN NAVIGATION
// ──────────────────────────────────────────────

function showScreen(screen) {
  [$intro, $quiz, $emailGate, $results].forEach(s => s.classList.remove('active'));
  screen.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'instant' });
}

// ──────────────────────────────────────────────
// QUIZ WIZARD
// ──────────────────────────────────────────────

function updateSelectedState() {
  // Show selected state if user already answered this question (e.g. navigating back)
  const prev = answers[currentQuestion];
  $btnYes.classList.toggle('selected', prev === true);
  $btnNo.classList.toggle('selected', prev === false);
}

function renderQuestion() {
  const q = QUESTIONS[currentQuestion];
  const total = QUESTIONS.length;

  // Progress
  const pct = ((currentQuestion) / total) * 100;
  $progressBar.style.width = pct + '%';
  $counter.textContent = `Question ${currentQuestion + 1} of ${total}`;

  // Back button visibility
  $backBtn.classList.toggle('hidden', currentQuestion === 0);

  // Question text
  $questionText.textContent = q.text;

  // Reset context
  contextOpen = false;
  $toggleCtx.classList.remove('open');
  $ctxBody.classList.remove('open');
  $ctxYes.textContent = q.yesContext;
  $ctxNo.textContent = q.noContext;

  // Show selected state for previously answered questions
  updateSelectedState();

  // Re-trigger card animation
  const card = document.querySelector('.question-card');
  card.style.animation = 'none';
  card.offsetHeight; // force reflow
  card.style.animation = '';
}

function answerQuestion(value) {
  answers[currentQuestion] = value;

  // Briefly highlight the selected button before advancing
  updateSelectedState();

  setTimeout(() => {
    if (currentQuestion < QUESTIONS.length - 1) {
      currentQuestion++;
      renderQuestion();
    } else {
      // All answered — show email gate
      $progressBar.style.width = '100%';
      showScreen($emailGate);
    }
  }, 150);
}

function goBack() {
  if (currentQuestion > 0) {
    currentQuestion--;
    renderQuestion();
  }
}

function toggleContext() {
  contextOpen = !contextOpen;
  $toggleCtx.classList.toggle('open', contextOpen);
  $ctxBody.classList.toggle('open', contextOpen);
}

// ──────────────────────────────────────────────
// SCORING
// ──────────────────────────────────────────────

function q(n) {
  // q(1) returns true/false for Question 1 (1-indexed)
  return answers[n - 1] === true;
}

function scoreOutcomes() {
  const scores = {};

  // Platform Play: Q1=YES AND Q10=YES AND (Q2=YES OR Q8=YES)
  scores['platform-play'] = {
    match: q(1) && q(10) && (q(2) || q(8)),
    strength: [q(1), q(10), q(2), q(8)].filter(Boolean).length
  };

  // Focused Wedge: Q5=YES AND Q12=YES AND (Q6=NO OR Q7=NO)
  scores['focused-wedge'] = {
    match: q(5) && q(12) && (!q(6) || !q(7)),
    strength: [q(5), q(12), !q(6), !q(7), q(9)].filter(Boolean).length
  };

  // Head-to-Head: Q2=YES AND Q3=YES AND Q6=YES AND Q7=YES AND (Q8=YES OR Q9=YES)
  scores['head-to-head'] = {
    match: q(2) && q(3) && q(6) && q(7) && (q(8) || q(9)),
    strength: [q(2), q(3), q(6), q(7), q(8), q(9)].filter(Boolean).length
  };

  // Create New Game: Q4=NO AND Q11=YES AND Q6=YES AND Q7=YES
  // Note: Q4=NO means buyers DON'T have an established name — that's the setup for category creation
  scores['create-new-game'] = {
    match: !q(4) && q(11) && q(6) && q(7),
    strength: [!q(4), q(11), q(6), q(7), !q(3)].filter(Boolean).length
  };

  return scores;
}

function detectHedgedRisk() {
  // Hedged positioning risk: Q6=NO AND Q7=NO but Q2=NO and Q10=YES
  if (!q(6) && !q(7) && !q(2) && q(10)) {
    return "Your answers suggest you're under-resourced (Q6, Q7) but horizontal (Q10) without a single unifying story (Q2). This combination often leads to volume sprawl — trying to cover too many angles without the team or budget to sustain them. Consider narrowing to a Focused Wedge first.";
  }
  // Additional sprawl signal: trying to go broad without resources
  if (!q(6) && !q(7) && !q(12)) {
    return "Your answers indicate limited resources and budget (Q6, Q7) combined with difficulty saying no to the TAM (Q12). This is a classic setup for hedged positioning and content sprawl. Committing to a narrow wedge will produce better results than spreading thin.";
  }
  return null;
}

function determineResult() {
  const scores = scoreOutcomes();

  // Find all matching outcomes
  const matches = Object.entries(scores)
    .filter(([, v]) => v.match)
    .sort((a, b) => b[1].strength - a[1].strength);

  // Find all non-matching outcomes ranked by strength (for fallback)
  const allRanked = Object.entries(scores)
    .sort((a, b) => b[1].strength - a[1].strength);

  let primary, secondary;

  if (matches.length >= 2) {
    primary = matches[0][0];
    secondary = matches[1][0];
  } else if (matches.length === 1) {
    primary = matches[0][0];
    // Secondary = next best non-matching
    const next = allRanked.find(([k]) => k !== primary);
    if (next && next[1].strength >= 2) {
      secondary = next[0];
    }
  } else {
    // No clean match — pick highest strength
    primary = allRanked[0][0];
    if (allRanked.length > 1 && allRanked[1][1].strength >= 2) {
      secondary = allRanked[1][0];
    }
  }

  const hedgedRisk = detectHedgedRisk();
  const noCleanMatch = matches.length === 0;

  return { primary, secondary, hedgedRisk, noCleanMatch };
}

// ──────────────────────────────────────────────
// RESULTS RENDERING
// ──────────────────────────────────────────────

function renderOutcomeCard(outcome) {
  const o = OUTCOMES[outcome];
  let html = '';

  // Who this works for
  html += `<div class="result-card">
    <h3><span class="section-icon">&#9673;</span> Who This Works For</h3>
    <ul>${o.whoFor.map(i => `<li>${i}</li>`).join('')}</ul>
  </div>`;

  // Why this makes sense
  html += `<div class="result-card">
    <h3><span class="section-icon">&#9670;</span> Why This Makes Sense</h3>
    <p>${o.whySense}</p>
  </div>`;

  // Content / GTM requirements
  html += `<div class="result-card">
    <h3><span class="section-icon">&#9881;</span> Content &amp; GTM Requirements</h3>
    <ul>${o.gtmRequirements.map(i => `<li>${i}</li>`).join('')}</ul>
  </div>`;

  // What you gain / lose
  html += `<div class="result-card card-gain">
    <h3><span class="section-icon">&#10003;</span> What You Gain</h3>
    <ul>${o.gains.map(i => `<li>${i}</li>`).join('')}</ul>
  </div>`;

  html += `<div class="result-card card-lose">
    <h3><span class="section-icon">&#10007;</span> What You Lose</h3>
    <ul>${o.losses.map(i => `<li>${i}</li>`).join('')}</ul>
  </div>`;

  // Examples
  html += `<div class="result-card">
    <h3><span class="section-icon">&#9733;</span> Examples</h3>
    <p>${o.examples}</p>
  </div>`;

  // Red flags
  html += `<div class="result-card card-fail">
    <h3><span class="section-icon">&#9888;</span> When This Fails (Red Flags)</h3>
    <ul>${o.redFlags.map(i => `<li>${i}</li>`).join('')}</ul>
  </div>`;

  // Workshop note
  html += `<div class="result-card">
    <h3><span class="section-icon">&#8594;</span> Workshop Connection</h3>
    <p>${o.workshopNote}</p>
  </div>`;

  return html;
}

function renderResults() {
  const { primary, secondary, hedgedRisk, noCleanMatch } = determineResult();
  const outcome = OUTCOMES[primary];

  // Set URL hash
  window.location.hash = `result=${primary}`;

  // Header
  document.getElementById('result-title').textContent = outcome.title;
  document.getElementById('result-subtitle').textContent = outcome.subtitle +
    (noCleanMatch ? ' Note: your answers didn\'t match a single clear pattern — this is the closest fit. Consider deeper analysis.' : '');

  // Primary result cards
  document.getElementById('result-primary').innerHTML = renderOutcomeCard(primary);

  // Hedged warning
  const $hedged = document.getElementById('hedged-warning');
  if (hedgedRisk) {
    document.getElementById('hedged-warning-text').textContent = hedgedRisk;
    $hedged.style.display = 'flex';
  } else {
    $hedged.style.display = 'none';
  }

  // Secondary result
  const $secondary = document.getElementById('secondary-result');
  if (secondary) {
    const secOutcome = OUTCOMES[secondary];
    document.getElementById('secondary-content').innerHTML =
      `<div class="result-card">
        <h3>${secOutcome.title}</h3>
        <p>${secOutcome.subtitle}</p>
        <p style="margin-top:0.75rem;"><strong>Why this also fits:</strong> ${secOutcome.whySense}</p>
      </div>`;
    $secondary.style.display = 'block';
  } else {
    $secondary.style.display = 'none';
  }

  // Answer summary
  const $answerList = document.getElementById('answer-list');
  $answerList.innerHTML = QUESTIONS.map((q, i) => {
    const val = answers[i];
    const label = val ? 'YES' : 'NO';
    const cls = val ? 'yes' : 'no';
    return `<div class="answer-row">
      <span class="answer-number">Q${i + 1}</span>
      <span class="answer-q">${q.text}</span>
      <span class="answer-val ${cls}">${label}</span>
    </div>`;
  }).join('');

  showScreen($results);
}

// ──────────────────────────────────────────────
// EMAIL FORM HANDLING
// ──────────────────────────────────────────────

async function handleEmailSubmit(e) {
  e.preventDefault();

  const name = document.getElementById('input-name').value.trim();
  const email = document.getElementById('input-email').value.trim();

  if (!name || !email) return;

  const submitBtn = $emailForm.querySelector('button[type="submit"]');
  submitBtn.textContent = 'Loading...';
  submitBtn.disabled = true;

  try {
    if (EMAIL_ENDPOINT) {
      // Send to configured endpoint
      await fetch(EMAIL_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email })
      });
    } else {
      // Dev mode — store locally
      try {
        localStorage.setItem('positioning-quiz-lead', JSON.stringify({ name, email, date: new Date().toISOString() }));
      } catch (_) { /* localStorage may be unavailable */ }
    }
  } catch (err) {
    // Don't block results on email submission failure
    console.warn('Email submission error:', err);
  }

  renderResults();
}

// ──────────────────────────────────────────────
// RETAKE / RESET
// ──────────────────────────────────────────────

function retake() {
  currentQuestion = 0;
  answers = [];
  contextOpen = false;
  window.location.hash = '';

  // Reset email form
  $emailForm.reset();
  const submitBtn = $emailForm.querySelector('button[type="submit"]');
  submitBtn.textContent = 'See My Results';
  submitBtn.disabled = false;

  showScreen($intro);
}

// ──────────────────────────────────────────────
// EVENT LISTENERS
// ──────────────────────────────────────────────

$startBtn.addEventListener('click', () => {
  showScreen($quiz);
  renderQuestion();
});

$btnYes.addEventListener('click', () => answerQuestion(true));
$btnNo.addEventListener('click', () => answerQuestion(false));
$backBtn.addEventListener('click', goBack);
$toggleCtx.addEventListener('click', toggleContext);
$emailForm.addEventListener('submit', handleEmailSubmit);
$retakeBtn.addEventListener('click', retake);

// Keyboard support
document.addEventListener('keydown', (e) => {
  // Only when quiz is active
  if (!$quiz.classList.contains('active')) return;

  if (e.key === 'y' || e.key === 'Y') {
    e.preventDefault();
    answerQuestion(true);
  } else if (e.key === 'n' || e.key === 'N') {
    e.preventDefault();
    answerQuestion(false);
  } else if (e.key === 'Backspace' || e.key === 'ArrowLeft') {
    e.preventDefault();
    goBack();
  }
});

// ──────────────────────────────────────────────
// INIT — check for hash-based result on load
// ──────────────────────────────────────────────

(function init() {
  // If URL has a result hash and we have stored answers, show results directly
  // Otherwise just show the intro
  showScreen($intro);
})();
