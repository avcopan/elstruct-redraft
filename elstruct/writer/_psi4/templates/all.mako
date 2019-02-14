#! ${comment}

memory ${memory} GB

##  1. molecule block
molecule mol {
${charge} ${mult}
${geom}
}

##  2. theoretical method block
set basis ${basis}

##      (a) scf method sub-block
${scf_options}
energy(${scf_method})

% if corr_method != '':
##      (a) main method sub-block, if it isn't SCF
set reference ${scf_method}
${corr_options}
energy(${corr_method})
% endif
