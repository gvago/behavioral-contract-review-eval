from threading import Event, Thread


def start_export(output, release):
    def run():
        release.wait()
        output.append('ready')
    thread = Thread(target=run, daemon=True)
    thread.start()
    return thread
