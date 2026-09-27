
"""
Is this not a builder-style class? The primary "construction" of a rigging will be done via the "Add Body Part" function.

This can take in any number of body parts, 
Each body part has:
1. A default orientation
2. A default "Attachment point" (used for rotation. Think of this like the anchor point in video-editing)
The attachment point is a number in relation to the center of the body part. For example, an Arm with a 0-0 attachment point would rotate around the elbow.
3. A default "Location from center". The "Center" is calculated dynamically as the center of the hitbox.
This means that Entities can belly-flop Ala a dead minecraft spider.
4. "Near/far/Z-Axis". Or, which sprites are ahead of other sprites.
5. A key_name. If I reuse my knight_arm .png for an armored spider's, I want to label that as a 
"""

"""
AI Prompt: I got thwarted by Usage limits.
@Иностранный Буквы/Mobs/Rigging.py:1-15 
Dew it. 
While "Doing it", I have requests: 
1.Splitting this up into two classes, the RiggingBuilder class & the Rigging is redundant. Improper rigging will be caught by The animation or the Action or something else.
2. Do not edit anything outside of Rigging.py. You may take a look at other files, but I would be annoyed at excess token use if you read anything outside of @Иностранный Буквы/Mobs/BodyPart.py .
3. I've de-facto implied that a either a rigging an animation or both has extra functions, I.E. for rotating.
Do not implement these functions.
"""