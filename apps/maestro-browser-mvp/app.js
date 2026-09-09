const STORAGE_KEY = "maestro-browser-mvp-v2";

const AXES = [
  ["theory", "Theory", "Tonal center, mode, harmony, meter, tempo, and structural theory."],
  ["voices", "Voices", "Lead, support, range, identity, assignments, and vocal relationships."],
  ["timbre", "Timbre", "Instrument and voice color, texture, density, and material character."],
  ["style", "Style", "Genre grammar, era, cultural lineage, references, and exclusions."],
  ["performance", "Performance", "Phrasing, dynamics, articulation, gestures, section execution, and staging."],
  ["postProduction", "Post-production", "Mix priorities, space, effects, imaging, editing, and mastering intent."],
  ["lyricsBlock", "Lyrics block", "Locked lyric text, section boundaries, assignments, ad-libs, SFX, and delivery cues."],
  ["end", "End", "Exit behavior, final cadence, fade or stop logic, and emotional closure."]
];

const AXIS_PREFIX = {
  theory: "THY",
  voices: "VOC",
  timbre: "TIM",
  style: "STY",
  performance: "PER",
  postProduction: "POST",
  lyricsBlock: "LYR",
  end: "MAP"
};

const emptyProject = () => ({
  version: 2,
  projectName: "",
  songTitle: "",
  creativeIntent: "",
  lyrics: "",
  instrumental: false,
  status: "draft",
  validation: null,
  lockedAt: null,
  selectedAxis: null,
  selectedAddress: null,
  technicalValues: {},
  evidence: [],
  axes: Object.fromEntries(AXES.map(([id]) => [id, { value: "", blocked: false, rationale: "" }]))
});

let state = loadState();
let saveTimer;
let runtimeAddresses = [];
let runtimeHealth = null;
let adherenceMatrix = null;

const byId = (id) => document.getElementById(id);
const fields = {
  projectName: byId("project-name"),
  songTitle: byId("song-title"),
  creativeIntent: byId("creative-intent"),
  lyrics: byId("lyrics"),
  instrumental: byId("instrumental")
};

function loadState() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return stored && stored.axes ? { ...emptyProject(), ...stored, technicalValues: stored.technicalValues || {}, evidence: stored.evidence || [] } : emptyProject();
  } catch {
    return emptyProject();
  }
}

function scheduleSave() {
  byId("save-state").textContent = "Saving…";
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    byId("save-state").textContent = "Saved locally";
  }, 180);
}

function escapeHtml(value = "") {
  return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[char]);
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    ...options,
    headers: { "Content-Type": "application/json", ...(options.headers || {}) }
  });
  const payload = await response.json().catch(() => ({ error: `HTTP ${response.status}` }));
  if (!response.ok) throw new Error(payload.error || `HTTP ${response.status}`);
  return payload;
}

function axisState(axis) {
  if (axis.blocked) return "blocked";
  if (axis.value.trim()) return "filled";
  return "null";
}

function metrics() {
  const values = Object.values(state.axes);
  const filled = values.filter((axis) => axisState(axis) === "filled").length;
  const blocked = values.filter((axis) => axisState(axis) === "blocked").length;
  return { filled, blocked, nulls: AXES.length - filled - blocked, progress: Math.round(((filled + blocked) / AXES.length) * 100) };
}

function addressesForAxis(id) {
  const prefix = AXIS_PREFIX[id];
  return runtimeAddresses.filter((item) => item.axis === prefix);
}

function ownerLabel(binding) {
  if (!binding) return "Runtime unresolved";
  return binding.primary_owner?.name || binding.primary_owner?.id || "Runtime unresolved";
}

function renderAxes() {
  byId("ust-grid").innerHTML = AXES.map(([id, label, description]) => {
    const axis = state.axes[id];
    const status = axisState(axis);
    const bindings = addressesForAxis(id);
    const authority = bindings.length ? `${bindings.length} runtime address${bindings.length === 1 ? "" : "es"}` : "runtime pending";
    return `<article class="panel ust-card" data-axis-card="${id}">
      <header><div><span class="axis-state">${status}</span><h3>${label}</h3></div><small>${escapeHtml(authority)}</small></header>
      <p>${description}</p>
      <textarea rows="6" data-axis-value="${id}" aria-label="${label} working note" placeholder="Working note for this axis. Lawful mutation occurs only at runtime-resolved Technical UST addresses." ${state.status === "locked" ? "disabled" : ""}>${escapeHtml(axis.value)}</textarea>
      <label class="checkbox-row"><input type="checkbox" data-axis-blocked="${id}" ${axis.blocked ? "checked" : ""} ${state.status === "locked" ? "disabled" : ""}><span>Blocked / deliberate null</span></label>
      <textarea rows="2" data-axis-rationale="${id}" aria-label="${label} rationale" placeholder="Required when blocked." ${state.status === "locked" ? "disabled" : ""}>${escapeHtml(axis.rationale)}</textarea>
      <div class="axis-actions"><button class="button button-secondary" type="button" data-dispatch-axis="${id}" ${bindings.length ? "" : "disabled"}>Open runtime addresses</button><button class="button button-secondary" type="button" data-clear="${id}" ${state.status === "locked" ? "disabled" : ""}>Clear note</button></div>
    </article>`;
  }).join("");

  document.querySelectorAll("[data-axis-value]").forEach((node) => node.addEventListener("input", (event) => updateAxis(event.target.dataset.axisValue, "value", event.target.value)));
  document.querySelectorAll("[data-axis-blocked]").forEach((node) => node.addEventListener("change", (event) => updateAxis(event.target.dataset.axisBlocked, "blocked", event.target.checked)));
  document.querySelectorAll("[data-axis-rationale]").forEach((node) => node.addEventListener("input", (event) => updateAxis(event.target.dataset.axisRationale, "rationale", event.target.value)));
  document.querySelectorAll("[data-dispatch-axis]").forEach((node) => node.addEventListener("click", () => selectAxis(node.dataset.dispatchAxis)));
  document.querySelectorAll("[data-clear]").forEach((node) => node.addEventListener("click", () => clearAxis(node.dataset.clear)));
}

function updateAxis(id, key, value) {
  state.axes[id][key] = value;
  if (key === "value" && value.trim()) state.axes[id].blocked = false;
  state.validation = null;
  scheduleSave();
  renderSummary();
}

function clearAxis(id) {
  state.axes[id] = { value: "", blocked: false, rationale: "" };
  state.validation = null;
  scheduleSave();
  render();
}

function renderQueue(filterAxis = null) {
  const visible = filterAxis ? addressesForAxis(filterAxis) : runtimeAddresses;
  const queue = visible.filter((binding) => !(binding.address in state.technicalValues));
  byId("queue-list").innerHTML = runtimeHealth?.ok
    ? (queue.length
      ? queue.map((binding) => `<div class="queue-item"><button type="button" data-queue-address="${escapeHtml(binding.address)}"><strong>${escapeHtml(binding.address)}</strong><br><small>${escapeHtml(ownerLabel(binding))} · runtime-resolved</small></button><span aria-hidden="true">→</span></div>`).join("")
      : `<p>No unresolved runtime address remains${filterAxis ? " in this axis" : ""}.</p>`)
    : `<p>Runtime authority is unavailable. Dispatch is fail-closed.</p>`;
  document.querySelectorAll("[data-queue-address]").forEach((node) => node.addEventListener("click", () => selectAddress(node.dataset.queueAddress)));
}

function selectAxis(id) {
  state.selectedAxis = id;
  state.selectedAddress = null;
  const [, label, description] = AXES.find(([axisId]) => axisId === id);
  const bindings = addressesForAxis(id);
  byId("dispatch-title").textContent = `${label} runtime addresses`;
  byId("dispatch-owner").textContent = bindings.length ? `${bindings.length} address-level authority binding${bindings.length === 1 ? "" : "s"} loaded from runtime.` : "No runtime binding loaded.";
  byId("dispatch-body").innerHTML = `<p>${description}</p><p><strong>Authority rule:</strong> the browser does not infer an owner from this axis. Select an exact Technical UST address; the runtime overlay decides its owner and reviewers.</p>`;
  renderQueue(id);
  scheduleSave();
}

async function selectAddress(address) {
  const binding = runtimeAddresses.find((item) => item.address === address) || await api(`/api/resolve?address=${encodeURIComponent(address)}`);
  state.selectedAddress = address;
  state.selectedAxis = AXES.find(([id]) => AXIS_PREFIX[id] === binding.axis)?.[0] || null;
  const reviewers = (binding.required_reviewers || []).map((item) => item.name || item.id).join(", ") || "none required";
  byId("dispatch-title").textContent = address;
  byId("dispatch-owner").textContent = `Runtime owner: ${ownerLabel(binding)}`;
  byId("dispatch-body").innerHTML = `<p><strong>Ownership source:</strong> ${escapeHtml(binding.ownership_source)}</p><p><strong>Required reviewers:</strong> ${escapeHtml(reviewers)}</p><p><strong>Bounded assignment:</strong> resolve only ${escapeHtml(address)}. Preserve project intent and do not infer authority for neighboring addresses.</p><button class="button button-primary" type="button" id="create-dispatch">Create lawful dispatch</button>`;
  byId("create-dispatch").addEventListener("click", () => createDispatch(binding));
  scheduleSave();
}

async function createDispatch(binding) {
  try {
    const packet = await api("/api/dispatch", {
      method: "POST",
      body: JSON.stringify({
        address: binding.address,
        task: `Resolve ${binding.address} for ${state.songTitle || state.projectName || "the current Maestro project"}. Preserve the stated creative intent and operate only within this Technical UST address.`,
        context_refs: ["technical.ust", "technical_ust_ownership_dependency_overlay.yaml"]
      })
    });
    const reviewers = packet.technical_ust?.required_reviewers?.join(", ") || "none";
    byId("dispatch-body").innerHTML = `<p><strong>Dispatch ready:</strong> ${escapeHtml(packet.dispatch_id)}</p><p><strong>Worker:</strong> ${escapeHtml(packet.worker_name)} (${escapeHtml(packet.worker_id)})</p><p><strong>Address:</strong> ${escapeHtml(packet.technical_ust.address)}</p><p><strong>Reviewers:</strong> ${escapeHtml(reviewers)}</p><p>${escapeHtml(packet.runtime_limit)}</p>`;
    showToast("Runtime-authorized dispatch created.");
  } catch (error) {
    showToast(`Dispatch blocked: ${error.message}`);
  }
}

function validate() {
  const issues = [];
  if (!runtimeHealth?.ok) issues.push("Technical UST runtime authority is unavailable.");
  if (!runtimeAddresses.length) issues.push("No runtime Technical UST addresses loaded.");
  if (!state.projectName.trim()) issues.push("Project name is required.");
  if (!state.songTitle.trim()) issues.push("Song title is required.");
  if (!state.creativeIntent.trim()) issues.push("Creative intent is required.");
  if (!state.instrumental && !state.lyrics.trim()) issues.push("Lyrics or source text are required unless the project is instrumental.");

  AXES.forEach(([id, label]) => {
    const axis = state.axes[id];
    if (!axis.value.trim() && !axis.blocked) issues.push(`${label} working note remains unresolved.`);
    if (axis.blocked && !axis.rationale.trim()) issues.push(`${label} is blocked without a rationale.`);
  });

  state.validation = { passed: issues.length === 0, issues, checkedAt: new Date().toISOString(), runtime: runtimeHealth };
  byId("validation-list").innerHTML = issues.length ? issues.map((issue) => `<li>${escapeHtml(issue)}</li>`).join("") : "<li>Browser intake gates pass and runtime authority is online. Axis notes are not treated as address-level ownership.</li>";
  byId("validation-status").textContent = issues.length ? "Fail" : "Pass";
  byId("lock-button").disabled = issues.length > 0 || state.status === "locked";
  scheduleSave();
  renderSummary();
  showToast(issues.length ? `${issues.length} gate issue${issues.length === 1 ? "" : "s"} found.` : "Validation passed.");
  return issues.length === 0;
}

function lockProject() {
  if (!validate()) return;
  state.status = "locked";
  state.lockedAt = new Date().toISOString();
  scheduleSave();
  render();
  showToast("Project locked locally. Runtime law remains external and authoritative.");
}

function startProject() {
  syncFields();
  state.status = "draft";
  state.validation = null;
  scheduleSave();
  render();
  showToast("Project started. Runtime Technical UST authority is active.");
}

function syncFields() {
  Object.entries(fields).forEach(([key, node]) => {
    state[key] = node.type === "checkbox" ? node.checked : node.value;
  });
}

function renderSummary() {
  const { filled, blocked, nulls, progress } = metrics();
  byId("progress-value").textContent = `${progress}%`;
  byId("progress-bar").style.width = `${progress}%`;
  byId("filled-count").textContent = filled;
  byId("blocked-count").textContent = blocked;
  byId("null-count").textContent = nulls;
  byId("workspace-title").textContent = state.songTitle || state.projectName || "Create a project to begin.";
  const runtimeText = runtimeHealth?.ok ? `Runtime online · ${runtimeAddresses.length} address bindings · ${runtimeHealth.renderer_adapter}` : "Runtime unavailable · dispatch fail-closed";
  byId("workspace-summary").textContent = state.creativeIntent ? `${state.creativeIntent} — ${runtimeText}` : runtimeText;
  byId("project-status").textContent = state.status === "locked" ? "Locked" : state.validation?.passed ? "Validated" : runtimeHealth?.ok ? "Runtime online" : "Runtime offline";
  byId("lock-button").disabled = !state.validation?.passed || state.status === "locked";

  document.querySelectorAll("#phase-list li").forEach((item) => item.classList.remove("active"));
  const activePhase = state.status === "locked" ? "lock" : nulls + blocked === 0 ? "resolution" : state.projectName ? "technical" : "intake";
  document.querySelector(`[data-phase="${activePhase}"]`)?.classList.add("active");
}

function renderValidation() {
  if (!state.validation) {
    byId("validation-status").textContent = "Not run";
    byId("validation-list").innerHTML = `<li>${runtimeHealth?.ok ? "Runtime authority is online." : "Runtime authority must be online before validation."}</li>`;
    return;
  }
  byId("validation-status").textContent = state.validation.passed ? "Pass" : "Fail";
  byId("validation-list").innerHTML = state.validation.issues.length ? state.validation.issues.map((issue) => `<li>${escapeHtml(issue)}</li>`).join("") : "<li>Browser intake gates pass and runtime authority is online.</li>";
}

function exportProject() {
  syncFields();
  const exportState = { ...state, runtimeSnapshot: { health: runtimeHealth, addresses: runtimeAddresses, adherenceMatrix } };
  const blob = new Blob([JSON.stringify(exportState, null, 2)], { type: "application/json" });
  const anchor = document.createElement("a");
  anchor.href = URL.createObjectURL(blob);
  anchor.download = `${(state.projectName || "maestro-project").replace(/[^a-z0-9]+/gi, "-").toLowerCase()}.json`;
  anchor.click();
  URL.revokeObjectURL(anchor.href);
}

function importProject(file) {
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const imported = JSON.parse(reader.result);
      if (!imported.axes) throw new Error("Missing axes");
      state = { ...emptyProject(), ...imported, axes: { ...emptyProject().axes, ...imported.axes }, technicalValues: imported.technicalValues || {}, evidence: imported.evidence || [] };
      scheduleSave();
      render();
      showToast("Project imported. Runtime authority was reloaded independently.");
    } catch {
      showToast("Import failed: invalid Maestro project JSON.");
    }
  };
  reader.readAsText(file);
}

function resetProject() {
  if (!confirm("Reset the browser-local Maestro project?")) return;
  state = emptyProject();
  localStorage.removeItem(STORAGE_KEY);
  render();
  showToast("Project reset.");
}

function showToast(message) {
  const toast = byId("toast");
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2400);
}

function render() {
  Object.entries(fields).forEach(([key, node]) => {
    if (node.type === "checkbox") node.checked = Boolean(state[key]);
    else node.value = state[key] || "";
    node.disabled = state.status === "locked";
  });
  byId("start-project").disabled = state.status === "locked";
  renderAxes();
  renderQueue(state.selectedAxis);
  renderSummary();
  renderValidation();
  if (state.selectedAddress) selectAddress(state.selectedAddress).catch(() => {});
  else if (state.selectedAxis) selectAxis(state.selectedAxis);
}

async function bootstrapRuntime() {
  try {
    const [health, addressPayload, matrix] = await Promise.all([
      api("/api/health"),
      api("/api/addresses"),
      api("/api/adherence-matrix")
    ]);
    runtimeHealth = health;
    runtimeAddresses = addressPayload.addresses || [];
    adherenceMatrix = matrix;
  } catch (error) {
    runtimeHealth = { ok: false, error: error.message };
    runtimeAddresses = [];
    adherenceMatrix = null;
  }
  render();
}

Object.values(fields).forEach((node) => node.addEventListener("input", () => { syncFields(); state.validation = null; scheduleSave(); renderSummary(); }));
byId("start-project").addEventListener("click", startProject);
byId("validate-button").addEventListener("click", validate);
byId("lock-button").addEventListener("click", lockProject);
byId("dispatch-next").addEventListener("click", () => {
  const pool = state.selectedAxis ? addressesForAxis(state.selectedAxis) : runtimeAddresses;
  const next = pool.find((binding) => !(binding.address in state.technicalValues));
  if (next) selectAddress(next.address); else showToast("No unresolved runtime address remains in this view.");
});
byId("export-button").addEventListener("click", exportProject);
byId("import-button").addEventListener("click", () => byId("import-file").click());
byId("import-file").addEventListener("change", (event) => event.target.files[0] && importProject(event.target.files[0]));
byId("reset-button").addEventListener("click", resetProject);

bootstrapRuntime();
