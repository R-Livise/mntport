import csv
import os

from report.models import Report

class ReportService:
  def __init__(self,table_name):
    self.table_name = table_name

  def create_report(self,report):
    with open(self.table_name, mode='a') as f:
      writer = csv.DictWriter(f,fieldnames=report.schema())
      writer.writerow(report.to_dict())

  def list_reports(self):
    with open(self.table_name, mode='r') as f:
      reader = csv.DictReader(f,fieldnames=Report.schema())

      return list(reader)

  def update_report(self,uptade_report):
    reports = self.list_reports()
    uptade_reports = []

    for report in reports:
      if report['uid'] == uptade_report.uid:
        uptade_reports.append(uptade_report.to_dict())
      else:
        uptade_reports.append(report)

        self._save_to_disk(uptade_reports)

  def delete_report(self,delete_report):
    reports = self.list_reports()
    delete_reports = []

    for report in reports:
      if report['uid'] != delete_report['uid']:
        delete_reports.append(report)

    self._save_to_disk(delete_reports)

  def _save_to_disk(self, reports):
    tmp_table_name = self.table_name + '.tmp'
    with open(tmp_table_name, mode='w') as f:
      writer = csv.DictWriter(f,fieldnames=Report.schema())
      writer.writerows(reports)

    os.remove(self.table_name)
    os.rename(tmp_table_name,self.table_name)