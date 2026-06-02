#!/usr/bin/env python3
import argparse
from pathlib import Path

TEMPLATE = """AFTER_CALL_FORMATTER\n\nMode: {mode}\nSource type: {source_type}\nNeeds transcription: {needs_transcription}\nSpeaker aware: {speaker_aware}\nSpeaker rename map: {speaker_rename_map}\nOutput depth: {output_depth}\nNeeds follow-up draft: {needs_follow_up}\nNeeds task extraction: {needs_tasks}\nExport format: {export_format}\nLanguage: {language}\nSpecial focus: {special_focus}\n\nRequested outcome:\n- {requested_outcome}\n\nImportant constraints:\n- {constraints}\n\nReturn structure:\n- {return_structure}\n"""


def infer_source_type(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix in {'.mp3', '.wav', '.m4a', '.aac'}:
        return 'audio'
    if suffix in {'.mp4', '.mov', '.mkv', '.webm'}:
        return 'video'
    if suffix in {'.txt', '.md'}:
        return 'transcript'
    return 'mixed'


def main():
    p = argparse.ArgumentParser(description='Build an AFTER_CALL_FORMATTER block')
    p.add_argument('--mode', required=True, choices=['work-call', 'therapy-session', 'client-follow-up', 'study-call'])
    p.add_argument('--source', help='Optional input file path to infer source type')
    p.add_argument('--source-type', choices=['audio', 'video', 'transcript', 'notes', 'mixed'])
    p.add_argument('--needs-transcription', choices=['yes', 'no'], default='no')
    p.add_argument('--speaker-aware', choices=['yes', 'no'], default='no')
    p.add_argument('--speaker-rename-map', default='none')
    p.add_argument('--output-depth', choices=['short', 'standard', 'deep'], default='standard')
    p.add_argument('--needs-follow-up', choices=['yes', 'no'], default='no')
    p.add_argument('--needs-tasks', choices=['yes', 'no'], default='yes')
    p.add_argument('--export-format', choices=['chat', 'telegram', 'obsidian', 'task-list', 'speaker-transcript'], default='chat')
    p.add_argument('--language', default='ru')
    p.add_argument('--special-focus', default='mixed')
    p.add_argument('--requested-outcome', default='Summarize the call clearly')
    p.add_argument('--constraints', default='Do not invent facts, owners, deadlines, or identities')
    p.add_argument('--return-structure', default='Short summary, core bullets, next steps')
    args = p.parse_args()

    source_type = args.source_type or (infer_source_type(args.source) if args.source else 'mixed')

    print(TEMPLATE.format(
        mode=args.mode,
        source_type=source_type,
        needs_transcription=args.needs_transcription,
        speaker_aware=args.speaker_aware,
        speaker_rename_map=args.speaker_rename_map,
        output_depth=args.output_depth,
        needs_follow_up=args.needs_follow_up,
        needs_tasks=args.needs_tasks,
        export_format=args.export_format,
        language=args.language,
        special_focus=args.special_focus,
        requested_outcome=args.requested_outcome,
        constraints=args.constraints,
        return_structure=args.return_structure,
    ))


if __name__ == '__main__':
    main()
