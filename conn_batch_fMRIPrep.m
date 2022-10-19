function conn_batch_fMRIPrep()
%
% batch processing script for the fmriprep dataset
% Mai 2022 - Marie Latil
% 
% Steps:
% Run conn_batch_fMRIPrep. The script will:
%      a) Find functional and structural files in the folders
%      b) Find masks and covariates files in the folders
%      c) Run Setup step
%      d) Run Denoising step
%      e) Run first-level analysis step :
%          Estimate first-level roi-to-roi and seed-to-voxel connectivity 
%          maps for each of the default seeds (located in the conn/rois 
%          folder), separately for each subject and for each of the three 
%          test-retest sessions.
%      f) Run all batch and display the results in conn gui

%% FIND functional/structural files
% note: this will look for all data in these folders
cd 'E:/Manip_IRM/fMRIPrep_outputs/fmriprep/';

NSUBJECTS=24; % 24 subjects in our dataset
nsessions=4; % one per resting (pre jour 1 - post jour 1 - pre jour 2 - post jour 2)
FUNCTIONAL_FILE={};
STRUCTURAL_FILE={};
data=[01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 20 21 22 23 24 25]; % number of the subjects in the folders, without number 19

FUNCTIONAL_FILE=cellstr(conn_dir(fullfile(pwd,'sub-*','ses-*','func','sub-*_ses-*_task-restp*_space-MNI152NLin6Asym_desc-smoothAROMAnonaggr_bold.nii.gz')));
STRUCTURAL_FILE=cellstr(conn_dir(fullfile(pwd,'sub-*','anat','sub-*_space-MNI152NLin6Asym_desc-preproc_T1w.nii.gz')));

ffsize=length(FUNCTIONAL_FILE);  % 96=24x4 : 24 subjects for 4 sessions (no subjects 19)
sfsize=length(STRUCTURAL_FILE);  % 24, 1 per subject

for i=ffsize:-1:NSUBJECTS*nsessions+1 % puts to 0 the files beyond the number of subjects we study (NUBJECTS)
    FUNCTIONAL_FILE(i,:)=[];
end

for i=sfsize:-1:NSUBJECTS+1 % puts to 0 the files beyond the number of subjects we study
    STRUCTURAL_FILE(i,:)=[];
end

if rem(length(FUNCTIONAL_FILE),NSUBJECTS),error('mismatch number of functional files %n', length(FUNCTIONAL_FILE));end % number of functional files should be a multiple of the number of subjects
if rem(length(STRUCTURAL_FILE),NSUBJECTS),error('mismatch number of anatomical files %n', length(FUNCTIONAL_FILE));end % number of structural files should be a multiple of the number of subjects

% reshape files in order to call them as FUNCTIONAL_FILE{nsub}{ses} or STRUCTURAL_FILE{nsub}
FUNCTIONAL_FILE=reshape(FUNCTIONAL_FILE,[nsessions,NSUBJECTS]).'; % reshape 96x1 --> NSUBJECTSx4 (nsessions=4)
STRUCTURAL_FILE={STRUCTURAL_FILE{1:NSUBJECTS}}; % reshape NSUBJECTSx1 --> 1xNSUBJECTS and delete files beyonde NSUBJECTS

% rename FUNCTIONAL_FILE (without the *)
nses=1; % sessions on conn, from 1 to 4
for nsub=1:NSUBJECTS
    for j=1:2 % 2 days (number of session in the folders)
        if nsub<10
            cd ("sub-0"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(FUNCTIONAL_FILE{nsub,nses})); % séparer chemin/nom/extension
            FUNCTIONAL_FILE{nsub,nses}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
            cd './../../../';
            cd ("sub-0"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(FUNCTIONAL_FILE{nsub,nses+1}));
            FUNCTIONAL_FILE{nsub,nses+1}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
        else
            cd ("sub-"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(FUNCTIONAL_FILE(nsub,nses)));
            FUNCTIONAL_FILE{nsub,nses}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
            cd './../../../';
            cd ("sub-"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(FUNCTIONAL_FILE{nsub,nses+1}));
            FUNCTIONAL_FILE{nsub,nses+1}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
        end
        cd './../../../';
        nses=nses+2;
        if nses>4
            nses=1;
        end
    end
end

% rename STRUCTURAL_FILE (without the *)
for nsub=1:NSUBJECTS
    if nsub<10
        cd ("sub-0"+data(nsub)+"/anat/");
        [a_path,a_name,a_ext]=fileparts(string(STRUCTURAL_FILE(nsub)));
        STRUCTURAL_FILE{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/anat/"+a_name+a_ext);
    else
        cd ("sub-"+data(nsub)+"/anat/");
        [a_path,a_name,a_ext]=fileparts(string(STRUCTURAL_FILE(nsub)));
        STRUCTURAL_FILE{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/anat/"+a_name+a_ext);
    end
    cd './../../';
end

disp([num2str(size(FUNCTIONAL_FILE,1)),' subjects']);
disp([num2str(size(FUNCTIONAL_FILE,2)),' sessions']);
TR=1.62; % Repetition time = 1.62 seconds

%% FIND masks/covariate matrix

cd 'E:/Manip_IRM/fMRIPrep_outputs/fmriprep/';

% MASKS
GREY = cellstr(conn_dir(fullfile(pwd,'sub-*','anat','sub-*M_label-GM_probseg.nii.gz'))); 
WHITE=cellstr(conn_dir(fullfile(pwd,'sub-*','anat','sub-*M_label-WM_probseg.nii.gz')));
CSF=cellstr(conn_dir(fullfile(pwd,'sub-*','anat','sub-*M_label-CSF_probseg.nii.gz'))); 
GREY={GREY{1:NSUBJECTS}};
WHITE={WHITE{1:NSUBJECTS}};
CSF={CSF{1:NSUBJECTS}};

msize=length(GREY);

for i=msize:-1:NSUBJECTS+1
    GREY(i,:)=[];
    WHITE(i,:)=[];
    CSF(i,:)=[];
end

% rename masks (without the *)
for nsub=1:NSUBJECTS
    if nsub<10
        cd ("sub-0"+data(nsub)+"/anat/");
        [a_path,a_name,a_ext]=fileparts(string(GREY(nsub)));
        GREY{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/anat/"+a_name+a_ext);
        [a_path,a_name,a_ext]=fileparts(string(WHITE(nsub)));
        WHITE{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/anat/"+a_name+a_ext);
        [a_path,a_name,a_ext]=fileparts(string(CSF(nsub)));
        CSF{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/anat/"+a_name+a_ext);
    else
        cd ("sub-"+data(nsub)+"/anat/");
        [a_path,a_name,a_ext]=fileparts(string(GREY(nsub)));
        GREY{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/anat/"+a_name+a_ext);
        [a_path,a_name,a_ext]=fileparts(string(WHITE(nsub)));
        WHITE{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/anat/"+a_name+a_ext);
        [a_path,a_name,a_ext]=fileparts(string(CSF(nsub)));
        CSF{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/anat/"+a_name+a_ext);
    end
    cd './../../';
end


% Brain mask - for GSR analysis
% BRAIN_MASK = cellstr(conn_dir(fullfile(pwd,'sub-*','anat','sub-*_space-MNI152NLin6Asym_desc-brain_mask.nii.gz'))); 
% BRAIN_MASK={BRAIN_MASK{1:NSUBJECTS}};
% 
% bsize=length(BRAIN_MASK);
% 
% for i=bsize:-1:NSUBJECTS+1
%     BRAIN_MASK(i,:)=[];
% end
% 
% % rename brain masks (without the *), for GSR analysis
% for nsub=1:NSUBJECTS
%     if nsub<10
%         cd ("sub-0"+data(nsub)+"/anat/");
%         [a_path,a_name,a_ext]=fileparts(string(BRAIN_MASK(nsub)));
%         BRAIN_MASK{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/anat/"+a_name+a_ext);
%     else
%         cd ("sub-"+data(nsub)+"/anat/");
%         [a_path,a_name,a_ext]=fileparts(string(BRAIN_MASK(nsub)));
%         BRAIN_MASK{nsub}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/anat/"+a_name+a_ext);
%     end
%     cd './../../';
% end


% COVARIATE
COVARIATE = cellstr(conn_dir(fullfile(pwd,'sub-*','ses-*','func','sub-*_ses-*_task-restp*_spm-regressors-AROMA.mat')));
csize=length(COVARIATE);

for i=csize:-1:NSUBJECTS*4+1
    COVARIATE(i,:)=[];
end

COVARIATE=reshape(COVARIATE,[nsessions,NSUBJECTS]).';

% rename masks (without the *)
nses=1;
for nsub=1:NSUBJECTS
    for j=1:2
        if nsub<10
            cd ("sub-0"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(COVARIATE{nsub,nses}));
            COVARIATE{nsub,nses}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
            cd './../../../';
            cd ("sub-0"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(COVARIATE{nsub,nses+1}));
            COVARIATE{nsub,nses+1}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-0"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
        else
            cd ("sub-"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(COVARIATE(nsub,nses)));
            COVARIATE{nsub,nses}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
            cd './../../../';
            cd ("sub-"+data(nsub)+"/ses-"+j+"/func/")
            [a_path,a_name,a_ext]=fileparts(string(COVARIATE{nsub,nses+1}));
            COVARIATE{nsub,nses+1}=convertStringsToChars("E:/Manip_IRM/fMRIPrep_outputs/fmriprep/sub-"+data(nsub)+"/ses-"+j+"/func/"+a_name+a_ext);
        end
        cd './../../../';
        nses=nses+2;
        if nses>4
            nses=1;
        end
    end
end

%% CONN-SPECIFIC SECTION: RUNS PREPROCESSING/SETUP/DENOISING/ANALYSIS STEPS
%% Prepares batch structure
clear batch;
batch.filename=fullfile('E:\Manip_IRM','conn_X_dynamic.mat');            % New conn_*.mat experiment name
%batch.filename=fullfile('E:\Manip_IRM','conn_X_gsr.mat');       % for GSR analysis

%% SETUP
% CONN Setup                                              % Default options (uses all ROIs in conn/rois/ directory); see conn_batch for additional options 
% CONN Setup.preprocessing                                  (realignment/coregistration/segmentation/normalization/smoothing)

batch.Setup.isnew=1;
batch.Setup.nsubjects=NSUBJECTS;
batch.Setup.RT=TR;                                        % TR (seconds)

% functional/structural files
batch.Setup.functionals=repmat({{}},[NSUBJECTS,1]);       % Point to functional volumes for each subject/session (put the files in cell array)
batch.Setup.acquisitiontype=1;                            % continu mode
 
for nsub=1:NSUBJECTS
    for nses=1:nsessions
        batch.Setup.functionals{nsub}{nses}=FUNCTIONAL_FILE{nsub,nses}; 
    end
    batch.Setup.structurals{nsub}=STRUCTURAL_FILE{nsub};  % Point to anatomical volumes for each subject
end

% nsubtest=3;
% for nses=1:nsessions
%     batch.Setup.functionals{nsubtest}{nses}=FUNCTIONAL_FILE{nsubtest,nses};
% end
%     batch.Setup.structurals{nsubtest}=STRUCTURAL_FILE{nsubtest};  % Point to anatomical volumes for each subject

% sessions
nconditions=nsessions;                                    % treats each session as a different condition
batch.Setup.conditions.names=[{'post1'}, {'pre1'}, {'post2'}, {'pre2'}];

for nsub=1:NSUBJECTS
    for ncond=1:nconditions
        for nses=1:nsessions
            if nses==ncond
                batch.Setup.conditions.onsets{ncond}{nsub}{nses}=0; 
                batch.Setup.conditions.durations{ncond}{nsub}{nses}=inf;
            else
                batch.Setup.conditions.onsets{ncond}{nsub}{nses}=[]; 
                batch.Setup.conditions.durations{ncond}{nsub}{nses}=[];
            end
        end
    end
end % session-specific conditions

% add this for dynamic connectivity
for ncond=1:nconditions
     batch.Setup.conditions.filter{ncond}=[81 0:40.5:486];       % no overlapp, just 7 windows
%      batch.Setup.conditions.filter{ncond}=[81 0:TR:288*TR];  % 288 windows
end 

% rois
% batch.Setup.rois.names={'Grey Matter','White Matter', 'CSF', 'atlas_conn','atlas_rois'}; % note: names of new ROIs ONLY here
batch.Setup.rois.names={'Grey Matter','White Matter', 'CSF','atlas_rois'}; % note: names of new ROIs ONLY here
for nsub=1:NSUBJECTS
    batch.Setup.rois.files{1}{nsub}=GREY{nsub};
    batch.Setup.rois.mask(1)=0; % no mask with grey matter
    batch.Setup.rois.files{2}{nsub}=WHITE{nsub};
    batch.Setup.rois.mask(2)=0; % no mask with grey matter
    batch.Setup.rois.files{3}{nsub}=CSF{nsub};
    batch.Setup.rois.mask(3)=0; % no mask with grey matter
end
% batch.Setup.rois.files{4}='C:\Users\baumontm\Documents\MATLAB\conn\rois\atlas.nii';
% batch.Setup.rois.mask(4)=1; % mask with grey matter
batch.Setup.rois.files{4}='E:\Manip_IRM\Atlas_roi\atlas_rois.nii';
batch.Setup.rois.mask(4)=1; % mask with grey matter

% if HMAT atlas wanted instead of conn atlas
% batch.Setup.rois.files{4}='E:\Manip_IRM\Atlas_HMAT\atlas_hmat.nii';
% batch.Setup.rois.mask(4)=1; % mask with grey matter

% rois for GSR analysis
% batch.Setup.rois.names={'Grey Matter','White Matter', 'CSF', 'Brain Mask','atlas','atlas_rois'}; % note: names of new ROIs ONLY here
% for nsub=1:NSUBJECTS
%     batch.Setup.rois.files{1}{nsub}=GREY{nsub};
%     batch.Setup.rois.mask(1)=0; % no mask with grey matter
%     batch.Setup.rois.files{2}{nsub}=WHITE{nsub};
%     batch.Setup.rois.mask(2)=0; % no mask with grey matter
%     batch.Setup.rois.files{3}{nsub}=CSF{nsub};
%     batch.Setup.rois.mask(3)=0; % no mask with grey matter
%     batch.Setup.rois.files{4}{nsub}=BRAIN_MASK{nsub};
%     batch.Setup.rois.mask(4)=0; % no mask with grey matter
% end
% batch.Setup.rois.files{5}='C:\Users\baumontm\Documents\MATLAB\conn\rois\atlas.nii';
% batch.Setup.rois.mask(5)=1; % mask with grey matter
% batch.Setup.rois.files{6}='E:\Manip_IRM\Atlas_roi\atlas_rois.nii';
% batch.Setup.rois.mask(6)=1; % mask with grey matter

% masks, non useful here
%batch.Setup.masks=repmat({},[NSUBJECTS,1]);    
% for nsub=1:NSUBJECTS
%     batch.Setup.masks.Grey{nsub}=GREY{nsub};
%     batch.Setup.masks.White{nsub}=WHITE{nsub};
%     batch.Setup.masks.CSF{nsub}=CSF{nsub};
% end

% covariate
batch.Setup.covariates.names={'mean_WM_CSF'};

for nsub=1:NSUBJECTS
    for nses=1:nsessions
        batch.Setup.covariates.files{1}{nsub}{nses}=COVARIATE{nsub,nses};
    end 
end

% setup
batch.Setup.analyses = [1,2]; % roi-to-roi and seed-to-voxel
batch.Setup.done=1;
batch.Setup.overwrite='Yes';  

% uncomment the following 3 lines if you prefer to run one step at a time:
% conn_batch (batch); % runs Preprocessing and Setup steps only
% clear batch;
% batch.filename=fullfile('E:\Manip_IRM','conn_X_dynamic.mat');            % Existing conn_*.mat experiment name

%% DENOISING step
% CONN Denoising                                    % Default options (uses White Matter+CSF+realignment+scrubbing+conditions as confound regressors); see conn_batch for additional options 

batch.Denoising.filter=[0.01, 0.08];                % frequency filter (band-pass values, in Hz)
batch.Denoising.confounds.names={'White Matter', 'CSF', 'Effect of post1', 'Effect of pre1', 'Effect of post2', 'Effect of pre2', 'mean_WM_CSF'};
%batch.Denoising.confounds.names={'White Matter', 'CSF', 'Effect of *', 'mean_WM_CSF'};
for nconfound=1:2,     batch.Denoising.confounds.dimensions{nconfound}=0; end
for nconfound=3:7,     batch.Denoising.confounds.dimensions{nconfound}=inf;   end

% for GSR analysis
% batch.Denoising.confounds.names={'White Matter', 'CSF', 'Brain Mask', 'Effect of post1', 'Effect of pre1', 'Effect of post2', 'Effect of pre2', 'mean_WM_CSF'};
% for nconfound=1:2,     batch.Denoising.confounds.dimensions{nconfound}=0; end
% for nconfound=3:8,     batch.Denoising.confounds.dimensions{nconfound}=inf;   end

batch.Denoising.done=1;
batch.Denoising.overwrite='Yes';

% uncomment the following 3 lines if you prefer to run one step at a time:
% conn_batch(batch); % runs Denoising step only
% clear batch;
% batch.filename=fullfile('E:\Manip_IRM','conn_X_dynamic.mat');            % Existing conn_*.mat experiment name

%% FIRST-LEVEL ANALYSIS step
% CONN Analysis                         % Default options (uses all ROIs in conn/rois/ as connectivity sources); see conn_batch for additional options 
batch.Analysis.measure=1;               % connectivity measure used {1 = 'correlation (bivariate)', 2 = 'correlation (semipartial)', 3 = 'regression (bivariate)', 4 = 'regression (multivariate)';
batch.Analysis.type=3;                  % analysis type, 1 = 'ROI-to-ROI', 2 = 'Seed-to-Voxel', 3 = 'all'; [3] 
batch.Analysis.sources={};              % (defaults to all ROIs)
batch.Analysis.weight=2;                % within-condition weight used {1 = 'none', 2 = 'hrf', 3 = 'hanning';
batch.Analysis.modulation=0;            % temporal modulation, 0 = standard weighted GLM analyses; 1 = gPPI analyses of condition-specific 
%                                         temporal modulation factor, or a string for PPI analyses of other temporal modulation factor 
%                                         (same for all conditions; valid strings are ROI names and 1st-level covariate names)'; [0] 
batch.Analysis.done=1;
batch.Analysis.overwrite='Yes';

%% Run all analyses
cd 'E:\Manip_IRM'
save('conn_X_dynamic.mat', 'batch');
% save('conn_X_gsr.mat', 'batch');      % for GSR analysis
conn_batch(batch);

%%
% batch.Results.display=1;                      % 1/0 display results [1]
% batch.Results.between_sources.effect_names= {'PC (Cingulate Gyrus, posterior division)'};
% batch.Results.between_sources.effect_names= {'Precuneous (Precuneous Cortex)'};

%% CONN Display
% launches conn gui to explore results
conn
cd './../../';
%conn('load',fullfile(cwd,'conn_X.mat'));
conn('load',batch.filename);
conn gui_results

end