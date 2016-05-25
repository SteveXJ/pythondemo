# -*- coding: utf-8 -*-
import sqlite3
import setting
import unittest
import HTMLTestRunner
import time

import TS_Catalogue.TC_Cust_Draft_SubtoApp as DraftToSubtoApp
import TS_Catalogue.TC_App1_SubtoApp_InPro1 as SubtoApptoInPro1
import TS_Catalogue.TC_IBM_SubtoIBM_AskForAmen as SubtoIBMtoAskForAme
import TS_Catalogue.TC_Creator_AskForAm_Amend_SubtoApp as AskForAmeToInitToSubToApp
import TS_Catalogue.TC_App1_SubtoApp_InPro1 as SubtoApptoInPro1
import TS_Catalogue.TC_App2_InPro1_InPro2 as InPro1toInPro2
import TS_Catalogue.TC_App3_InPro2_SubtoIBM as InPro2toSubtoIBM
import TS_Catalogue.TC_IBM_SubtoIBM_Acknow as SubtoIBMtoAcknow
import TS_Catalogue.TC_IBMOPE_Acknow_Proce as AcknowtoPro
import TS_Catalogue.TC_IBMDepMgr_Draft_Proposed as DraftToProposed
import TS_Catalogue.TC_App2_Draft_SubtoIBM as App2DraftToSubIBM

import TS_Deployment.TC_Cust_Draft_Submitted as CusDraftToSubmitted
import TS_Deployment.TC_App1_Submitted_InPro1 as SubtoDeploy
import TS_Deployment.TC_App1_Submitted_InPro1 as SubtoInPro1
import TS_Deployment.TC_App2_InPro1_InPro2 as InPr1toInPr2
import TS_Deployment.TC_App3_InPro2_Deployed as InPr2toDeploy
import TS_Deployment.TC_IBMDepMgr_Draft_Proposal as DraftToProposal
import TS_Deployment.TC_App1_Proposal_InPro1 as ProposalToDeploy
import TS_Deployment.TC_App1_Proposal_InPro1 as ProtoInPro1
import TS_Deployment.TC_App2_Draft_Deployed as App2NeedisNO

setting.init()
suite = unittest.TestSuite()
#####################START  Send to first approver and Single approver START#############################
###1. Catalogue WorkFlow 2. Customer Create   ###
## Status: Draft--SubtoApp--SubtoIBM--AskForAmend--Amend--Init--SubtoApp--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(DraftToSubtoApp.Cust_Draft_SubtoApp)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Catalogue WorkFlow 2. IBMDeployMgr Create  ###
### Status: Draft--SubtoApp--SubtoIBM--AskForAmend--Amend--Init--SubtoApp--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(DraftToProposed.IBMDepMgr_Draft_Proposed)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Catalogue WorkFlow 2. Approver2 Create 3.Approver need is NO ###
### Status: Draft--SubtoIBM--AskForAmend--Amend--Init--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(App2DraftToSubIBM.Applevel2_Draft_SubtoIBM)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

##1. Deployment WorkFlow 2. Customer Create   ###
# Status: Draft--Submitted--Deployed
# suite.addTest(unittest.makeSuite(CusDraftToSubmitted.DraftToSubmitted)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoDeploy.SubmittedToApproved1))

# ##1. Deployment WorkFlow 2. IBMDeployMgr Create  ###
# ## Status: Draft--Proposal--Deployed
# suite.addTest(unittest.makeSuite(DraftToProposal.DraftToProposal)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(ProposalToDeploy.ProposalToApproved1))

# ##1. Catalogue WorkFlow 2. Approver2 Create 3.Approver need is NO ###
# ## Status: Draft--Deployed
# suite.addTest(unittest.makeSuite(App2NeedisNO.DraftToDeployed))

#####################END Send to first approver and Single approver END#############################

#####################START  Send to first approver and Mulit approver START#############################
###1. Catalogue WorkFlow 2. Customer Create   ###
### Status: Draft--SubtoApp--InPro1--InPro2--SubtoIBM--AskForAmend--Amend--Init--SubtoApp--InPro1--InPro2--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(DraftToSubtoApp.Cust_Draft_SubtoApp)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Catalogue WorkFlow 2. IBMDeployMgr Create  ###
### Status: Draft--SubtoApp--InPro1--InPro2--SubtoIBM--AskForAmend--Amend--Init--SubtoApp--InPro1--InPro2--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(DraftToProposed.IBMDepMgr_Draft_Proposed)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Catalogue WorkFlow 2. Approver2 Create 3.Approver need is NO ###
## Status: Draft--SubtoIBM--AskForAmend--Amend--Init--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(App2DraftToSubIBM.Applevel2_Draft_SubtoIBM)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Deployment WorkFlow 2. Customer Create   ###
## Status: Draft--Submitted--Deployed
# suite.addTest(unittest.makeSuite(CusDraftToSubmitted.DraftToSubmitted)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoInPro1.SubmittedToApproved1))
# suite.addTest(unittest.makeSuite(InPr1toInPr2.Approved1ToApproved2))
# suite.addTest(unittest.makeSuite(InPr2toDeploy.Approved2ToDeployed))

# ###1. Deployment WorkFlow 2. IBMDeployMgr Create  ###
# ### Status: Draft--Proposal--Deployed
# suite.addTest(unittest.makeSuite(DraftToProposal.DraftToProposal)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(ProtoInPro1.ProposalToApproved1))
# suite.addTest(unittest.makeSuite(InPr1toInPr2.Approved1ToApproved2))
# suite.addTest(unittest.makeSuite(InPr2toDeploy.Approved2ToDeployed))

# ###1. Catalogue WorkFlow 2. Approver2 Create 3.Approver need is NO ###
# ### Status: Draft--Deployed
# suite.addTest(unittest.makeSuite(App2NeedisNO.DraftToDeployed))
#####################END  Send to first approver and Mulit approver END#############################

#####################START  Send to next approver and Mulit approver START#############################
###1. Catalogue WorkFlow 2. Customer Create   ###
### Status: Draft--SubtoApp--InPro1--InPro2--SubtoIBM--AskForAmend--Amend--Init--SubtoApp--InPro1--InPro2--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(DraftToSubtoApp.Cust_Draft_SubtoApp)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Catalogue WorkFlow 2. IBMDeployMgr Create  ###
# ### Status: Draft--SubtoApp--InPro1--InPro2--SubtoIBM--AskForAmend--Amend--Init--SubtoApp--InPro1--InPro2--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(DraftToProposed.IBMDepMgr_Draft_Proposed)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(InPro1toInPro2.App2_InPro1_InPro2))
# suite.addTest(unittest.makeSuite(InPro2toSubtoIBM.App3_InPro2_SubtoIBM))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Catalogue WorkFlow 2. Approver2 Create 3.Approver need is NO ###
# ## Status: Draft--SubtoIBM--AskForAmend--Amend--Init--SubtoIBM--Acknow--Processed
# suite.addTest(unittest.makeSuite(App2DraftToSubIBM.Applevel2_Draft_SubtoIBM)) #makeSuite(FileName.ClassName)
# suite.addTest(unittest.makeSuite(SubtoIBMtoAskForAme.SubmittedToAmendment))
# suite.addTest(unittest.makeSuite(AskForAmeToInitToSubToApp.AmendmentToSubtoapp))
# suite.addTest(unittest.makeSuite(SubtoApptoInPro1.App1_SubtoApp_InPro1))
# suite.addTest(unittest.makeSuite(SubtoIBMtoAcknow.SubmittedToAcknowledged))
# suite.addTest(unittest.makeSuite(AcknowtoPro.AcknowledgedToProcessed))

###1. Deployment WorkFlow 2. Customer Create   ###
# Status: Draft--Submitted--Deployed
suite.addTest(unittest.makeSuite(CusDraftToSubmitted.DraftToSubmitted)) #makeSuite(FileName.ClassName)
suite.addTest(unittest.makeSuite(SubtoInPro1.SubmittedToApproved1))
suite.addTest(unittest.makeSuite(InPr1toInPr2.Approved1ToApproved2))
suite.addTest(unittest.makeSuite(InPr2toDeploy.Approved2ToDeployed))

###1. Deployment WorkFlow 2. IBMDeployMgr Create  ###
### Status: Draft--Proposal--Deployed
suite.addTest(unittest.makeSuite(DraftToProposal.DraftToProposal)) #makeSuite(FileName.ClassName)
suite.addTest(unittest.makeSuite(ProtoInPro1.ProposalToApproved1))
suite.addTest(unittest.makeSuite(InPr1toInPr2.Approved1ToApproved2))
suite.addTest(unittest.makeSuite(InPr2toDeploy.Approved2ToDeployed))

###1. Catalogue WorkFlow 2. Approver2 Create 3.Approver need is NO ###
### Status: Draft--Deployed
suite.addTest(unittest.makeSuite(App2NeedisNO.DraftToDeployed))
#####################END Send to next approver and Mulit approver END#############################

#TestResult report
report_Name = str(time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time())))
filename = "./TestResult/" + report_Name + ".html" #tagart path and file name
fp = file(filename, 'wb')
#TestResult Report description
runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u'Esmt Auto-Test Report', description = u'Test_Report')
runner.run(suite)