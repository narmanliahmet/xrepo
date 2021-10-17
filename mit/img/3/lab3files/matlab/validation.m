function validation
%VALIDATION  Validate brain segmentation against an expert
%  This function validates your brain segmentation against that of the expert.
%
%  You must modify in the variables CLASSIFICATION_PREFIX and BRAIN_PREFIX to
%  point to the data path that you used for MRI segment classification.

% Last modified: 4/06/06, Eric Weiss


% Update your path prefixes here
%-------------------------------
CLASSIFICATION_PREFIX = '/mit/6.555/....../output/classification';
BRAIN_PREFIX = '/mit/6.555/....../output/brain';


% MRI path and image specifications (do not modify)
%--------------------------------------------------
MRI_PREFIX = '/mit/6.555/data/seg/swrot/spgr/I';
LABELS_PREFIX = '/mit/6.555/data/seg/swrot/segtruth/I';
LABEL_WHITE = 8;
LABEL_GRAY = 4;
LABEL_CSF = 5;
TEST_SLICE = 130;


% Read and display your result for the test slice
%------------------------------------------------
my_result_fn =  sprintf('%s.%0.3d', BRAIN_PREFIX, TEST_SLICE);
my_result = mri_read(my_result_fn);


% Read and display the expert's result for the test slice
%--------------------------------------------------------
gold_standard_fn = sprintf('%s.%0.3d', LABELS_PREFIX, TEST_SLICE);
gold_standard = mri_read(gold_standard_fn);


% Plot results
%-------------
figure; display_image(my_result,'My Result');
figure; display_image(gold_standard,'Expert Result');
