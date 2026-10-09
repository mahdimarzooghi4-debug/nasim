/** Existing authorized Case-only historical records; NOT Outcome or Provider decisions. */
import { api, canReadCases } from "./api";
import type {
  ActorContext, AssignmentView, ObservationView, TimelineEntry,
} from "./types";
import type { InteractionRecorded } from "./correctionCommands";

export type HistoryKind = "timeline" | "assignments" | "interactions" | "observations";
export type HistoryPage =
  | { kind: "timeline"; items: TimelineEntry[]; next_cursor: string | null }
  | { kind: "assignments"; items: AssignmentView[]; next_cursor: null }
  | { kind: "interactions"; items: InteractionRecorded[]; next_cursor: string | null }
  | { kind: "observations"; items: ObservationView[]; next_cursor: string | null };

export function mayReadCaseHistory(actor: ActorContext): boolean {
  return actor.actor_type === "HUMAN" && canReadCases(actor);
}

export async function readCaseHistory(
  kind: HistoryKind, caseId: string, cursor: string | null,
  signal?: AbortSignal,
): Promise<HistoryPage> {
  // Backend rechecks Case read + current assignment for EVERY request;
  // no earlier successful query is reused as authorization.
  if (kind === "timeline") {
    const page = await api.timeline(caseId, cursor, signal);
    return { kind, ...page };
  }
  if (kind === "assignments") {
    const items = await api.assignments(caseId, signal);
    return { kind, items, next_cursor: null };
  }
  if (kind === "interactions") {
    const page = await api.interactions(caseId, cursor, signal);
    return { kind, ...page };
  }
  const page = await api.observations(caseId, cursor, signal);
  return { kind: "observations", ...page };
}
