#!/bin/bash
set -o pipefail -o errexit -o nounset
cd $(dirname ${BASH_SOURCE[0]})

# Spaceship leaving colony:
video_id=I4zto6KRnWQ
yt-dlp -f 'best[filesize<300M]' https://www.youtube.com/watch?v=$video_id
#   ffmpeg takes ~10s to complete:
ffmpeg -ss 00:00:15 -i *$video_id*.* -to 00:01:50 -c:a copy -y "FallingFrontier-ExclusiveMightOfMars.mp4"
rm *$video_id*.*

# Spaceship arriving to space station:
video_id=t-dxN6VU-Io
yt-dlp https://www.youtube.com/watch?v=$video_id
#   Hide final part of the video with a black screen (ffmpeg takes ~5s to complete):
ffmpeg -i *$video_id*.* -vf "drawbox=enable='between(t,28,40)':color=black:t=fill" -to 00:31:00 -c:a copy -y "EndersGameBattleSchool.webm"
rm *$video_id*.*

# A monster is coming...
video_id=l5WeBNfX-og
yt-dlp https://www.youtube.com/watch?v=$video_id
#   ffmpeg takes ~5min to complete:
ffmpeg -ss 00:00:02 -i *$video_id*.* -to 00:00:39 -c:a copy -y "DeadSpace-Trailer2021.webm"
rm *$video_id*.*

# Skiping the last one, great but too linked with The Expanse universe:
exit 0

# Mentions Mars, the Belt, Earth imperialism, a planetary alert...
video_id=CufoAulgXfU
yt-dlp https://www.youtube.com/watch?v=$video_id
#   Hide final part of the video with a black screen:
ffmpeg -ss 00:00:34 -i *$video_id*.* -vf "drawbox=enable='between(t,36,41)':color=black:t=fill" -to 00:00:41 -c:a copy -y "TheExpanse-Season3-OpeningScene.webm"
rm *$video_id*.*
