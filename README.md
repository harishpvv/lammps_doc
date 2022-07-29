# lammps_doc
Lammps documentation in JupyterNotebooks

Find the path of LAMMPS HTML documentation folder. Generally, it will be in `<lammps>/doc/html/`. Then set,

` export $LAMMPS_HTML_PATH=<lammps_html_path>`

Then use JupyterNotebooks, like,

```python
import lammps_doc as ld

ld.get_syntax('fix_nve')
ld.get_description('fix_nve')
ld.get_get_examples('fix_nve')
ld.list_commands()

```
