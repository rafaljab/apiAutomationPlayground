from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import subprocess


@method_decorator(csrf_exempt, name="dispatch")
class DeployWebhookView(View):
    def post(self, request, *args, **kwargs):
        auth_header = request.headers.get("X-Deploy-Token")

        if not auth_header or auth_header != settings.DEPLOY_TOKEN:
            return JsonResponse({"error": "Unauthorized"}, status=401)

        try:
            # We are running this on PythonAnywhere, so the base dir is the project root
            project_dir = settings.BASE_DIR

            # The deploy command to execute locally on the PythonAnywhere server
            deploy_script = (
                "git pull origin master && uv sync --no-dev --group prod "
                "&& uv run manage.py migrate "
                "&& uv run manage.py collectstatic --noinput"
            )

            # Use Popen/run to execute the shell command
            result = subprocess.run(
                deploy_script,
                shell=True,
                cwd=project_dir,
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                return JsonResponse({"status": "success", "output": result.stdout})
            else:
                return JsonResponse(
                    {"status": "error", "error": result.stderr}, status=500
                )

        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)}, status=500)
