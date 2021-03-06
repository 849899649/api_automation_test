from django.conf.urls import url

from api_test.api import ApiDoc, automationCase as Case, member, dynamic, user
from api_test.api.global_parameter import host_total, add_host, update_host, del_host, enable_host, disable_host
from api_test.api.projectList import project_list, add_project, update_project, del_project, disable_project, \
     enable_project
from api_test.api.projectTitle import project_info

urlpatterns = [
    url(r'project/project_list', project_list),
    url(r'project/add_project', add_project),
    url(r'project/update_project', update_project),
    url(r'project/del_project', del_project),
    url(r'project/disable_project', disable_project),
    url(r'project/enable_project', enable_project),
    url(r'title/project_info', project_info),
    url(r'global/host_total', host_total),
    url(r'global/add_host', add_host),
    url(r'global/update_host', update_host),
    url(r'global/del_host', del_host),
    url(r'global/disable_host', disable_host),
    url(r'global/enable_host', enable_host),
    url(r'api/group', ApiDoc.group),
    url(r'api/add_group', ApiDoc.add_group),
    url(r'api/update_name_group', ApiDoc.update_name_group),
    url(r'api/del_group', ApiDoc.del_group),
    url(r'api/api_list', ApiDoc.api_list),
    url(r'api/add_api', ApiDoc.add_api),
    url(r'api/update_api', ApiDoc.update_api),
    url(r'api/del_api', ApiDoc.del_api),
    url(r'api/update_group', ApiDoc.update_group),
    url(r'api/api_info', ApiDoc.api_info),
    url(r'api/add_history', ApiDoc.add_history),
    url(r'api/history_list', ApiDoc.history_list),
    url(r'api/del_history', ApiDoc.del_history),
    url(r'api/operation_history', ApiDoc.operation_history),
    url(r'api/Download', ApiDoc.download),
    url(r'api/download_doc', ApiDoc.download_doc),
    url(r'automation/group', Case.group),
    url(r'automation/add_group', Case.add_group),
    url(r'automation/del_group', Case.del_group),
    url(r'automation/update_name_group', Case.update_name_group),
    url(r'automation/update_case_group', Case.update_case_group),
    url(r'automation/case_list', Case.case_list),
    url(r'automation/add_case', Case.add_case),
    url(r'automation/update_case', Case.update_case),
    url(r'automation/del_case', Case.del_case),
    url(r'automation/api_list', Case.api_list),
    url(r'automation/api_info', Case.api_info),
    url(r'automation/add_new_api', Case.add_new_api),
    url(r'automation/get_correlation_response', Case.get_correlation_response),
    url(r'automation/add_old_api', Case.add_old_api),
    url(r'automation/update_api', Case.update_api),
    url(r'automation/del_api', Case.del_api),
    url(r'automation/start_test', Case.start_test),
    url(r'automation/add_time_task', Case.add_time_task),
    url(r'automation/get_time_task', Case.get_task),
    url(r'automation/del_task', Case.del_task),
    url(r'automation/look_result', Case.look_result),
    url(r'automation/test_report', Case.test_report),
    url(r'automation/auto_test_report', Case.auto_test_report),
    url(r'automation/test_time', Case.test_time),
    url(r'member/project_member', member.project_member),
    url(r'dynamic/dynamic', dynamic.dynamic),
    url(r'user/login', user.obtain_auth_token),
]
