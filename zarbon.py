import subprocess


class Zarbon:
    def __getattr__(self, main_cmd: str,):
        self.main_cmd = main_cmd
        return self.main_processing


    def get_cmd(self, args):
        args_str = list(args)
        cmd = [self.main_cmd]
        cmd.extend(args_str)
        return cmd


    def execute(self):
        subprocess.run(self.cmd)


    def main_processing(self, *args):
        self.cmd = self.get_cmd(args)
        self.execute()
        return self


    def __or__(self, other):
        pass

