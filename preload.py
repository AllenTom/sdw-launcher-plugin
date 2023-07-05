def preload(parser):
    parser.add_argument("--launcher-session", type=str, help="launcher session", default="global")
    parser.add_argument("--launcher-callback", type=str, help="launcher session", default="http://localhost:6745")