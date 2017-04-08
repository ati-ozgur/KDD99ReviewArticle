from __future__ import print_function

import ReviewHelper
import pandas as pd


output_constants = ""

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

totalNumberOfArticles = df["ID"].count()
string_to_print = "\\newcommand{{\\totalNumberOfArticles}}{{{0}}}".format(totalNumberOfArticles)
output_constants = output_constants + string_to_print + "\n"

totalNumberOfJournals = len(df["journal"].unique())
string_to_print = "\\newcommand{{\\totalNumberOfJournals}}{{{0}}}".format(totalNumberOfJournals)
output_constants = output_constants + string_to_print + "\n"

metainformationIDS = df.metaIDSType.value_counts()["IDS"]
string_to_print = "\\newcommand{{\\metainformationIDS}}{{{0}}}".format(metainformationIDS)
output_constants = output_constants + string_to_print + "\n"


metainformationNotIDS = df.metaIDSType.value_counts()["NotIDS"]
string_to_print = "\\newcommand{{\\metainformationNotIDS}}{{{0}}}".format(metainformationNotIDS)
output_constants = output_constants + string_to_print + "\n"

metainformationML = sum(df.metaIDSTechnology.str.contains("MachineLearning"))
string_to_print = "\\newcommand{{\\metainformationML}}{{{0}}}".format(metainformationML)
output_constants = output_constants + string_to_print + "\n"



row_filter_ML_and_IDS = ((df.metaIDSType == "IDS") & (df.metaIDSTechnology.str.contains("MachineLearning")))
metainformationMLandIDS = df[row_filter_ML_and_IDS]["ID"].count()
string_to_print = "\\newcommand{{\\metainformationMLandIDS}}{{{0}}}".format(metainformationMLandIDS)
output_constants = output_constants + string_to_print + "\n"

row_filter_ML_and_NotIDS = ((df.metaIDSType == "NotIDS") & (df.metaIDSTechnology.str.contains("MachineLearning")))
metainformationMLandNotIDS = df[row_filter_ML_and_NotIDS]["ID"].count()
string_to_print = "\\newcommand{{\\metainformationMLandNotIDS}}{{{0}}}".format(metainformationMLandNotIDS)
output_constants = output_constants + string_to_print + "\n"

metainformationDatasetTrainingAndTraining = df[df.metaTrainingSet.str.contains("KDD99Training")].ID.count()
string_to_print = "\\newcommand{{\\metainformationDatasetTrainingAndTraining}}{{{0}}}".format(metainformationDatasetTrainingAndTraining)
output_constants = output_constants + string_to_print + "\n"



metainformationDatasetTrainingAndTest = df[df.metaTrainingSet.str.contains("KDD99Test")].ID.count()
string_to_print = "\\newcommand{{\\metainformationDatasetTrainingAndTest}}{{{0}}}".format(metainformationDatasetTrainingAndTest)
output_constants = output_constants + string_to_print + "\n"

metainformationDatasetTestAndTraining = df[df.metaTestSet.str.contains("KDD99Training")].ID.count()
string_to_print = "\\newcommand{{\\metainformationDatasetTestAndTraining}}{{{0}}}".format(metainformationDatasetTestAndTraining)
output_constants = output_constants + string_to_print + "\n"


metainformationDatasetTestAndTest = df[df.metaTestSet.str.contains("KDD99Test")].ID.count()
string_to_print = "\\newcommand{{\\metainformationDatasetTestAndTest}}{{{0}}}".format(metainformationDatasetTestAndTest)
output_constants = output_constants + string_to_print + "\n"

metainformationDatasetTestAndTestPercentage = metainformationDatasetTestAndTest * 100 / totalNumberOfArticles
string_to_print = "\\newcommand{{\\metainformationDatasetTestAndTestPercentage}}{{{0}}}".format(metainformationDatasetTestAndTestPercentage)
output_constants = output_constants + string_to_print + "\n"

metainformationCrossValidationYes = df[df.metaCrossValidation == "Yes"].ID.count()
string_to_print = "\\newcommand{{\\metainformationCrossValidationYes}}{{{0}}}".format(metainformationCrossValidationYes)
output_constants = output_constants + string_to_print + "\n"

metainformationCrossValidationYesPercentage = metainformationCrossValidationYes * 100 / totalNumberOfArticles
string_to_print = "\\newcommand{{\\metainformationCrossValidationYesPercentage}}{{{0}}}".format(metainformationCrossValidationYesPercentage)
output_constants = output_constants + string_to_print + "\n"


metainformationCrossValidationNo = df[df.metaCrossValidation == "No"].ID.count()
string_to_print = "\\newcommand{{\\metainformationCrossValidationNo}}{{{0}}}".format(metainformationCrossValidationNo)
output_constants = output_constants + string_to_print + "\n"

metainformationCrossValidationNoPercentage = 100 - metainformationCrossValidationYesPercentage
string_to_print = "\\newcommand{{\\metainformationCrossValidationNoPercentage}}{{{0}}}".format(metainformationCrossValidationNoPercentage)
output_constants = output_constants + string_to_print + "\n"



row_filter_KDDLargeClaim =  (( df.comment.notnull()) & (df.comment.str.contains("KDD99LargeClaim")))
metainformationKDDLargeClaim = df[row_filter_KDDLargeClaim]["ID"].count()
string_to_print = "\\newcommand{{\\metainformationKDDLargeClaim}}{{{0}}}".format(metainformationKDDLargeClaim)
output_constants = output_constants + string_to_print + "\n"


start_year = "2010"
end_year = "2016"
string_to_print = "\\newcommand{{\\focusedPeriod}}{{{start_year}--{end_year}}}".format(start_year = start_year,end_year=end_year)
output_constants = output_constants + string_to_print + "\n"

string_to_print = "\\newcommand{{\\focusedPeriodBetween}}{{{start_year} and {end_year}}}".format(start_year = start_year,end_year=end_year)
output_constants = output_constants + string_to_print + "\n"


dfTrainingSizes = ReviewHelper.get_pandas_data_frame_dataset_sizes_training()
smallestCount = 20
smallestTrainingDatasetSizeFirstCount = dfTrainingSizes[1:smallestCount].min()[0] 
largestTrainingDatasetSizeFirstCount = dfTrainingSizes[1:smallestCount].max()[0]

metainformationSmallestCount = smallestCount
string_to_print = "\\newcommand{{\\metainformationSmallestCount}}{{{0}}}".format(metainformationSmallestCount)
output_constants = output_constants + string_to_print + "\n"

string_to_print = "\\newcommand{{\\smallestTrainingDatasetSizeFirstCount}}{{{0}}}".format(smallestTrainingDatasetSizeFirstCount)
output_constants = output_constants + string_to_print + "\n"

string_to_print = "\\newcommand{{\\largestTrainingDatasetSizeFirstCount}}{{{0}}}".format(largestTrainingDatasetSizeFirstCount)
output_constants = output_constants + string_to_print + "\n"


dfTestingSizes = ReviewHelper.get_pandas_data_frame_dataset_sizes_testing()
smallestTestingDatasetSizeFirstCount = dfTestingSizes[1:smallestCount].min()[0] 
largestTestingDatasetSizeFirstCount = dfTestingSizes[1:smallestCount].max()[0]

string_to_print = "\\newcommand{{\\smallestTestingDatasetSizeFirstCount}}{{{0}}}".format(smallestTestingDatasetSizeFirstCount)
output_constants = output_constants + string_to_print + "\n"

string_to_print = "\\newcommand{{\\largestTestingDatasetSizeFirstCount}}{{{0}}}".format(largestTestingDatasetSizeFirstCount)
output_constants = output_constants + string_to_print + "\n"


IDSdatasetISCXUsageCount = ReviewHelper.get_other_dataset_usage_count("ISCX")
string_to_print = "\\newcommand{{\\IDSdatasetISCXUsageCount}}{{{0}}}".format(IDSdatasetISCXUsageCount)
output_constants = output_constants + string_to_print + "\n"

IDSdatasetKyotoUsageCount = ReviewHelper.get_other_dataset_usage_count("Kyoto")
string_to_print = "\\newcommand{{\\IDSdatasetKyotoUsageCount}}{{{0}}}".format(IDSdatasetKyotoUsageCount)
output_constants = output_constants + string_to_print + "\n"


otherIDSdatasetUsageCount = ReviewHelper.get_other_ids_datasets_usage_count_apart_from_darpa()
string_to_print = "\\newcommand{{\\otherIDSdatasetUsageCount}}{{{0}}}".format(otherIDSdatasetUsageCount)
output_constants = output_constants + string_to_print + "\n"


countPerformanceMetricTrainingTime = df.metaPerformanceMetrics.str.contains("TrainingTime").sum()
string_to_print = "\\newcommand{{\\countPerformanceMetricTrainingTime}}{{{0}}}".format(countPerformanceMetricTrainingTime)
output_constants = output_constants + string_to_print + "\n"

countPerformanceMetricTrainingTimePercentage = countPerformanceMetricTrainingTime * 100 / totalNumberOfArticles
string_to_print = "\\newcommand{{\\countPerformanceMetricTrainingTimePercentage}}{{{0}}}".format(countPerformanceMetricTrainingTimePercentage)
output_constants = output_constants + string_to_print + "\n"


countPerformanceMetricTestingTime = df.metaPerformanceMetrics.str.contains("TestingTime").sum()
string_to_print = "\\newcommand{{\\countPerformanceMetricTestingTime}}{{{0}}}".format(countPerformanceMetricTestingTime)
output_constants = output_constants + string_to_print + "\n"

countPerformanceMetricTestingTimePercentage = countPerformanceMetricTestingTime * 100 / totalNumberOfArticles
string_to_print = "\\newcommand{{\\countPerformanceMetricTestingTimePercentage}}{{{0}}}".format(countPerformanceMetricTestingTimePercentage)
output_constants = output_constants + string_to_print + "\n"


#print(output_constants)

filename = "../latex/constants.tex"
target = open(filename, 'w')
target.write(output_constants)
target.close()

