// Gutter Math engine - hypothetical arithmetic on labeled norms only.
// Section, seam, downspout and slope figures are illustrative norms;
// roof shape, rainfall and corner cuts change real runs.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function seamTruth(feet, section) {
  if (!(feet > 0)) throw new Error("the run must be above zero");
  if (!(section > 0)) throw new Error("the section length must be above zero");
  const sections = Math.ceil(feet / section - 1e-9);
  const seams = Math.max(0, sections - 1);
  let verdict;
  if (seams <= 2) verdict = "barely any drips honestly";
  else if (seams <= 8) verdict = "a few future drips honestly";
  else if (seams <= 20) verdict = "a row of future drips honestly";
  else verdict = "a whole choir of drips honestly";
  return `${feet} ${plural(feet, "foot", "feet")} of eave against the ${section}-foot section claim is ${sections} ${plural(sections, "section", "sections")} and ${seams} ${plural(seams, "seam", "seams")} - ${verdict}.`;
}

function spoutTruth(area, norm) {
  if (!(area > 0)) throw new Error("the roof area must be above zero");
  if (!(norm > 0)) throw new Error("the downspout norm must be above zero");
  const spouts = Math.ceil(area / norm - 1e-9);
  let verdict;
  if (spouts === 1) verdict = "a single downspout honestly";
  else if (spouts <= 3) verdict = "a modest set honestly";
  else if (spouts <= 6) verdict = "a working set honestly";
  else verdict = "a downspout on every corner honestly";
  return `${area} ${plural(area, "square foot", "square feet")} of roof against the ${norm}-square-foot downspout norm is ${spouts} ${plural(spouts, "downspout", "downspouts")} - ${verdict}.`;
}

function slopeTruth(feet, rate) {
  if (!(feet > 0)) throw new Error("the run must be above zero");
  if (!(rate > 0)) throw new Error("the slope norm must be above zero");
  const fall = feet * rate / 10;
  const rounded = Math.round(fall * 10) / 10;
  let verdict;
  if (rounded === 0) verdict = "barely a fall honestly";
  else if (rounded <= 1) verdict = "a gentle fall honestly";
  else if (rounded <= 3) verdict = "a working fall honestly";
  else verdict = "a determined fall honestly";
  const fallPart = rounded === 0 ? "less than a tenth of an inch" : `${fixed1(fall)} ${plural(rounded === 1 ? 1 : 2, "inch", "inches")}`;
  return `${feet} ${plural(feet, "foot", "feet")} at the ${rate}-inch-per-ten-feet slope norm falls ${fallPart} toward the downspout - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { seamTruth, spoutTruth, slopeTruth };
}
