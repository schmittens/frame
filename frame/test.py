__author__ = 'split'

from assets.helper import * #projects_lister, project_collector

p = project_collector('beispiel')
g = project_gallery(p)
print(g.images)


