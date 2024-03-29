#!/bin/bash
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

raw.getMessageCount() {
    return ${#_allMessages[@]}
}

raw.getAllMessages() {
    echo ${_allMessages[@]}
}

raw.getLastMessage() {
    if test ${#_allMessages[@]} -gt 0; then
        ${_allMessages[-1]}.$1 "$2"
    elif [[ -n $BOT_TOKEN && -n $LOG_CHANNEL_ID ]]; then
        log "first sendMessage ! (caused by \"core.methods.$FUNCNAME\")\n"$2""
    else
        log "$2"
    fi
}
