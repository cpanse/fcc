import getopt
import sys
import fcc

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hoepl", [
                                   "help", "output=", "exec", "pattern=", "loop", "hostname=", "ncpu="])
    except getopt.GetoptError as err:
        print (str(err))
        usage()
        sys.exit(2)

    fcc = fcc.Fcc()

    for o, value in opts:
        if o == "--output":
            fcc.set_para('myOutputFile', value)
        elif o == "--exec":
            fcc.set_para('exec', True)
        elif o == "--loop":
            fcc.set_para('loop', True)
        elif o == "--pattern":
            fcc.set_para('myPattern', value)
        elif o == "--hostname":
            myHostname = value
        elif o == "--ncpu":
            fcc.set_para('ncpu',  int(value))
        elif o in ("--help"):
            usage()
            sys.exit(0)
        else:
            usage()
            sys.exit(1)

    crawl_pattern = ['/srv/www/htdocs/Data2San/',
        'p[0-9]{2,4}', 'Metabolomics',
        '(GCT|G2HD)_[0-9]',
        '[a-z]{3,18}_[0-9]{8}(_[-a-zA-Z0-9_]{0,100}){0,1}',
        '[-a-zA-Z0-9_]+.(raw|RAW|wiff|wiff\.scan)']

    fcc.set_para('crawl_pattern', crawl_pattern)
    fcc.run()
