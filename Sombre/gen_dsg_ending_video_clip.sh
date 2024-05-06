#!/bin/bash
set -o pipefail -o errexit -o nounset
cd $(dirname ${BASH_SOURCE[0]})

video_id=SgRUmUQqSYc
yt-dlp https://www.youtube.com/watch?v=$video_id
ffmpeg -ss 00:01:28 -i *$video_id*.* -to 00:01:27 -c:a copy -y "DeadSpaceGore-Ending.webm"
rm *$video_id*.*
