#!/bin/bash
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT
trap 'echo hi' USR1

initKannaX() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing KannaX ..."
    assertEnvironment
    editLastMessage "Starting KannaX ..."
    printLine
}

startKannaX() {
    startLogBotPolling
    runPythonModule kannax "$@"
}

stopKannaX() {
    sendMessage "Exiting KannaX ..."
    endLogBotPolling
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopKannaX
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopKannaX
    exit 130
}

runKannaX() {
    initKannaX
    startKannaX "$@"
    local code=$?
    stopKannaX
    return $code
}
