UnTagger
UnTagger is a utility designed to scrub unwanted tags and metadata from your audio and video files.

We all know the frustration of downloading files from platforms like YouTube, Spotify, or Amazon Music, only to find them cluttered with extra data—source links, branding, encoder details, or random comments. Over time, this makes media libraries look messy and inconsistent.

UnTagger exists to fix that. The goal is simply to keep your media library clean, regardless of where the files came from.

What it does: The tool strips away platform-related clutter from both audio and video files. Rather than just blocking specific site names, it focuses on identifying patterns to separate junk data from the useful metadata you actually want to preserve. It is designed to be lightweight and easy to extend.

We are building this step by step, starting with a manual approach and gradually working toward intelligent automation.

Project Structure
To keep things organized, UnTagger is being developed across two main branches.

1. The manual branch (The stable foundation)

This represents how UnTagger works right now. It is strictly rule-based. We explicitly define what counts as "junk" based on known patterns. There is no AI or guessing involved here—just transparent, predictable behavior. This branch serves as the baseline for correctness and a fallback if more complex methods fail.

2. The ai branch (Experimental)

This branch is where we look at making UnTagger smarter. The plan is to integrate a model trained on examples of dirty versus clean metadata. Over time, we want the software to learn which fields are unnecessary based on real-world inputs and outputs, rather than relying solely on hardcoded rules.

The AI isn't replacing the manual logic immediately. Instead, it will sit on top of it, learning gradually to improve accuracy and adapt to new tagging patterns.

Why separate them?
Keeping the manual and AI logic in different branches ensures that the core tool remains stable and trustworthy. It makes debugging easier and allows you to use the standard version of UnTagger without ever needing to touch the experimental AI components.

Current Status and Vision
Right now, the core logic and manual detection are in progress, while the AI integration is still in the planning and experimental phase.

Long term, the vision is for UnTagger to become a universal cleaner that works across all formats. We want it to learn from usage while remaining transparent—users should never feel like they are using a "black box" tool.

License
To be decided.
