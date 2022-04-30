import pyfuscator
from pathlib import (Path)
import sys
import subprocess

this_dir = Path(__file__).parent.resolve()
test_in_dir = this_dir / 'test_inputs'
test_out_dir = this_dir / 'test_outputs'

def main():
    for out in test_out_dir.glob('*'):
        if out.name == '.gitignore':
            continue
        out.unlink()

    for org_py in test_in_dir.glob('*.py'):
        print('==== Testing', org_py)
        out_base = test_out_dir / org_py.name
        obf_py = out_base.with_suffix('.obf.py')
        pyfuscator.obfuscate(org_py, obf_py)

        org_out = out_base.with_suffix('.org.out')
        obf_out = out_base.with_suffix('.obf.out')

        for py, out in [(org_py, org_out),
                        (obf_py, obf_out)]:
            r = subprocess.run([sys.executable, py], capture_output=True, text=True)
            with open(out, 'w') as f:
                print(f'exit code = {r.returncode}\n---------- stdout:\n{r.stdout}\n---------- stderr:\n{r.stderr}', file=f)

        subprocess.check_call(['diff', '-u', org_out, obf_out])

if __name__ == '__main__':
    main()
