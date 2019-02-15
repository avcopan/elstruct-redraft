## 0. job/computation block
#! ${comment}
memory ${memory} GB
${job_options}

##  1. molecule block
molecule {
${charge} ${mult}
${geom}
% if zmat_vals != '':
${zmat_vals}
% endif
}

##  2. theoretical method block
set basis ${basis}

##      (a) scf method sub-block
${scf_options}
set reference ${scf_method}
energy('scf')

% if corr_method != '':
##      (a) main method sub-block, if it isn't SCF
${corr_options}
energy('${corr_method}')
% endif
