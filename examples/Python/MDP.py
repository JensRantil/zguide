"""Majordomo Protocol definitions"""
#  This is the version of MDP/Client we implement
C_CLIENT = "MDPC02"

#  This is the version of MDP/Worker we implement
W_WORKER = "MDPW02"

#  MDP/Client commands, as strings
C_REQUEST       =   "\001"
C_PARTIAL       =   "\002"
C_FINAL         =   "\003"

#  MDP/Worker commands, as strings
W_READY         =   "\001"
W_REQUEST       =   "\002"
W_PARTIAL       =   "\003"
W_FINAL         =   "\004"
W_HEARTBEAT     =   "\005"
W_DISCONNECT    =   "\006"

commands = [None, "READY", "REQUEST", "PARTIAL", "FINAL", "HEARTBEAT",
            "DISCONNECT"]
