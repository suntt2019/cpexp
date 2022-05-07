import cpexp.generated.CPExpListener


class PrintListener(cpexp.generated.CPExpListener.CPExpListener):
    def enterP(self, ctx):
        print('enter p', ctx)

    def exitP(self, ctx):
        print('exit p', ctx)
