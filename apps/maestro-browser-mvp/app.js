const STORAGE_KEY = "maestro-browser-mvp-v1";

const AXES = [
  ["theory", "Theory", "Tonal center, mode, harmony, meter, tempo, and structural theory.", "Canon"],
  ["voices", "Voices", "Lead, support, range, identity, assignments, and vocal relationships.", "Vanessa"],
  ["timbre", "Timbre", "Instrument and voice color, texture, density, and material character.", "Analog Confessor"],
  ["style", "Style", "Genre grammar, era, cultural lineage, references, and exclusions.", "Mo"],
  ["performance", "Performance", "Phrasing, dynamics, articulation, gestures, section execution, and staging.", "Metro"],
  ["postProduction", "Post-production", "Mix priorities, space, effects, imaging, editing, and mastering intent.", "Eldrik"],
  ["lyricsBlock", "Lyrics block", "Locked lyric text, section boundaries, assignments, ad-libs, SFX, and delivery cues.", "Sage"],
  ["end", "End", "Exit behavior, final cadence, fade or stop logic, and emotional closure.", "Alan"]
];

const emptyProject = () => ({
  version: 1,
  projectName: "",
  songTitle: "",
  creativeIntent: "",
  lyrics: "",
  instrumental: false,
  status: "draft",
  validation: null,
  lockedAt: null,
  selectedAxis: null,
  axes: Object.fromEntries(AXES.map(([id]) => [id, { value: "", blocked: false, rationale: "" }]))
});

let state = loadState();
let saveTimer;

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
    return stored && stored.axes ? { ...emptyProject(), ...stored } : emptyProject();
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
  return value.replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[char]);
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

function renderAxes() {
  byId("ust-grid").innerHTML = AXES.map(([id, label, description, owner]) => {
    const axis = state.axes[id];
    const status = axisState(axis);
    return `<article class="panel ust-card" data-axis-card="${id}">
      <header><div><span class="axis-state">${status}</span><h3>${label}</h3></div><small>${owner}</small></header>
      <p>${description}</p>
      <textarea rows="6" data-axis-value="${id}" aria-label="${label} value" placeholder="Address this axis or defend the null." ${state.status === "locked" ? "disabled" : ""}>${escapeHtml(axis.value)}</textarea>
      <label class="checkbox-row"><input type="checkbox" data-axis-blocked="${id}" ${axis.blocked ? "checked" : ""} ${state.status === "locked" ? "disabled" : ""}><span>Blocked / deliberate null</span></label>
      <textarea rows="2" data-axis-rationale="${id}" aria-label="${label} rationale" placeholder="Required when blocked." ${state.status === "locked" ? "disabled" : ""}>${escapeHtml(axis.rationale)}</textarea>
      <div class="axis-actions"><button class="button button-secondary" type="button" data-dispatch="${id}">Dispatch address</button><button class="button button-secondary" type="button" data-clear="${id}" ${state.status === "locked" ? "disabled" : ""}>Clear</button></div>
    </article>`;
  }).join("");

  document.querySelectorAll("[data-axis-value]").forEach((node) => node.addEventListener("input", (event) => updateAxis(event.target.dataset.axisValue, "value", event.target.value)));
  document.querySelectorAll("[data-axis-blocked]").forEach((node) => node.addEventListener("change", (event) => updateAxis(event.target.dataset.axisBlocked, "blocked", event.target.checked)));
  document.querySelectorAll("[data-axis-rationale]").forEach((node) => node.addEventListener("input", (event) => updateAxis(event.target.dataset.axisRationale, "rationale", event.target.value)));
  document.querySelectorAll("[data-dispatch]").forEach((node) => node.addEventListener("click", () => selectAxis(node.dataset.dispatch)));
  document.querySelectorAll("[data-clear]").forEach((node) => node.addEventListener("click", () => clearAxis(node.dataset.clear)));
}

function updateAxis(id, key, value) {
  state.axes[id][key] = value;
  if (key === "value" && value.trim()) state.axes[id].blocked = false;
  state.validation = null;
  scheduleSave();
  renderSummary();
  renderQueue();
}

function clearAxis(id) {
  state.axes[id] = { value: "", blocked: false, rationale: "" };
  state.validation = null;
  scheduleSave();
  render();
}

function renderQueue() {
  const unresolved = AXES.filter(([id]) => axisState(state.axes[id]) !== "filled");
  byId("queue-list").innerHTML = unresolved.length
    ? unresolved.map(([id, label, , owner]) => `<div class="queue-item"><button type="button" data-queue-axis="${id}"><strong>${label}</strong><br><small>${owner} · ${axisState(state.axes[id])}</small></button><span aria-hidden="true">→</span></div>`).join("")
    : `<p>All Technical UST addresses are filled.</p>`;
  document.querySelectorAll("[data-queue-axis]").forEach((node) => node.addEventListener("click", () => selectAxis(node.dataset.queueAxis)));
}

function selectAxis(id) {
  state.selectedAxis = id;
  const [, label, description, owner] = AXES.find(([axisId]) => axisId === id);
  byId("dispatch-title").textContent = label;
  byId("dispatch-owner").textContent = `Lawful owner: ${owner}`;
  byId("dispatch-body").innerHTML = `<p>${description}</p><p><strong>Bounded assignment:</strong> Resolve only this axis. Preserve the project intent and do not infer values for other axes.</p><button class="button button-primary" type="button" id="focus-axis">Open ${label}</button>`;
  byId("focus-axis").addEventListener("click", () => {
    document.querySelector(`[data-axis-card="${id}"]`).scrollIntoView({ behavior: "smooth", block: "center" });
    document.querySelector(`[data-axis-value="${id}"]`).focus();
  });
  scheduleSave();
}

function validate() {
  const issues = [];
  if (!state.projectName.trim()) issues.push("Project name is required.");
  if (!state.songTitle.trim()) issues.push("Song title is required.");
  if (!state.creativeIntent.trim()) issues.push("Creative intent is required.");
  if (!state.instrumental && !state.lyrics.trim()) issues.push("Lyrics or source text are required unless the project is instrumental.");

  AXES.forEach(([id, label]) => {
    const axis = state.axes[id];
    if (!axis.value.trim() && !axis.blocked) issues.push(`${label} remains unresolved.`);
    if (axis.blocked && !axis.rationale.trim()) issues.push(`${label} is blocked without a rationale.`);
  });

  state.validation = { passed: issues.length === 0, issues, checkedAt: new Date().toISOString() };
  byId("validation-list").innerHTML = issues.length ? issues.map((issue) => `<li>${escapeHtml(issue)}</li>`).join("") : "<li>All intake and Technical UST gates pass.</li>";
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
  showToast("Project locked in browser-local storage.");
}

function startProject() {
  syncFields();
  state.status = "draft";
  state.validation = null;
  scheduleSave();
  render();
  showToast("Project started. Technical UST addresses are open.");
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
  byId("workspace-summary").textContent = state.creativeIntent || "The browser stores one editable project, its Technical UST, gate state, and lock record.";
  byId("project-status").textContent = state.status === "locked" ? "Locked" : state.validation?.passed ? "Validated" : "Draft";
  byId("lock-button").disabled = !state.validation?.passed || state.status === "locked";

  document.querySelectorAll("#phase-list li").forEach((item) => item.classList.remove("active"));
  const activePhase = state.status === "locked" ? "lock" : nulls + blocked === 0 ? "resolution" : state.projectName ? "technical" : "intake";
  document.querySelector(`[data-phase="${activePhase}"]`)?.classList.add("active");
}

function renderValidation() {
  if (!state.validation) {
    byId("validation-status").textContent = "Not run";
    byId("validation-list").innerHTML = "<li>Start the project, then validate its intake and Technical UST state.</li>";
    return;
  }
  byId("validation-status").textContent = state.validation.passed ? "Pass" : "Fail";
  byId("validation-list").innerHTML = state.validation.issues.length ? state.validation.issues.map((issue) => `<li>${escapeHtml(issue)}</li>`).join("") : "<li>All intake and Technical UST gates pass.</li>";
}

function exportProject() {
  syncFields();
  const blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
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
      state = { ...emptyProject(), ...imported, axes: { ...emptyProject().axes, ...imported.axes } };
      scheduleSave();
      render();
      showToast("Project imported.");
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
  renderQueue();
  renderSummary();
  renderValidation();
  if (state.selectedAxis) selectAxis(state.selectedAxis);
}

Object.values(fields).forEach((node) => node.addEventListener("input", () => { syncFields(); state.validation = null; scheduleSave(); renderSummary(); }));
byId("start-project").addEventListener("click", startProject);
byId("validate-button").addEventListener("click", validate);
byId("lock-button").addEventListener("click", lockProject);
byId("dispatch-next").addEventListener("click", () => {
  const next = AXES.find(([id]) => axisState(state.axes[id]) !== "filled");
  if (next) selectAxis(next[0]); else showToast("No unresolved address remains.");
});
byId("export-button").addEventListener("click", exportProject);
byId("import-button").addEventListener("click", () => byId("import-file").click());
byId("import-file").addEventListener("change", (event) => event.target.files[0] && importProject(event.target.files[0]));
byId("reset-button").addEventListener("click", resetProject);

render();
