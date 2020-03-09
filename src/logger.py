import util
import sys
import traceback
from os.path import basename, os
import logging
import shutil


def init_logger(filelogPath,
                isUseWindow=False,
                isWorker=True):
    formatter = logging.Formatter("[%(asctime)s.%(msecs)03d %(process)d])%(message)s(%(levelno)s)",
                                  datefmt="%Y-%m-%d %H:%M:%S")

    Log = logging.getLogger('')
    Log.setLevel(logging.INFO)
    Log.propagate = False

    if isUseWindow:
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        Log.addHandler(console)
        write_info_log("Consloe Log Start")

    filelog = logging.FileHandler(filelogPath,
                                  mode='w',
                                  encoding='utf-8')
    filelog.setFormatter(formatter)
    Log.addHandler(filelog)

    if not isWorker:
        write_info_log("File logging start")

    return Log

# TODO Need to modify clearly


def moveLogFile(fileLogPath,
                filelogName,
                filelogDir):
    writeLog(1,
             "Clean logging file")
    beforeate = str(util.getBeforeDaytime())
    filelogDir = filelogDir + "/" + beforeate

    if not os.path.exists(filelogDir):
        os.makedirs(filelogDir)
        writeLog(1,
                 "Make new directory : {0}".format(filelogDir))

    fileLogMovePath = filelogDir + "/" + filelogName
    if not os.path.exists(fileLogMovePath):
        shutil.move(fileLogPath, filelogDir)
        writeLog(1,
                 "Move logging file")
    else:
        writeLog(1,
                 "Logging file is already exist")


def release_logger(Log):
    writeLog(1,
             "End logging")
    try:
        del Log.handlers[:]
        return True

    except:
        writeLog(1,
                 "Fail to end logging")
        return False
    logging.shutdown()


def writeLog(level, text):
    logging.log(level, "(%d):%s" % (level, text))


def write_info_log(text):
    logging.info("[INFO] %s" % text)


def write_warning_log(text):
    logging.warning("[WARN] %s" % text)


def write_critical_log(text):
    logging.critical("[CRIT] %s" % text)


def write_error_log(text):
    logging.error("[ERROR] %s" % text)


def writePacket(packetkey, text):
    if packetkey is 1:
        outstring = "\n".join(text)

    elif packetkey is 2:
        dictlist = []
        for key, value in text.iteritems():
            temp = str(key) + " : " + str(value)
            dictlist.append(temp)
        outstring = "\n".join(dictlist)

    else:
        write_critical_log("Input key error")
        return

    write_info_log("Packet dump detail >> \n%s" % (outstring))


def writeException(ex):
    stack_trace = traceback.extract_tb(sys.exc_info()[2])
    first = True
    for filename, lineno, ftnname, _ in reversed(stack_trace):
        if first:
            write_error_log("Exception : %s:%s(%d) %s %s" %
                            (basename(filename),
                             ftnname,
                             lineno,
                             type(ex),
                                ex))
            first = False

        else:
            write_error_log("Call stack : %s:%s(%d)" %
                            (basename(filename),
                             ftnname,
                             lineno))
