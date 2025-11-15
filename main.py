from models.template_data import TemplateData
from models.component import Component
from models.script import Script
from models.rollback_script import RollbackScript
from models.step import Step
from models.rollback_plan import RollbackPlan
from models.verification import Verification
from models.approver import Approver
from models.enums import DeploymentType, ComponentType, ScriptType

from services.template_services import TemplateService


def main():
    print(DeploymentType.REQUERIMIENTO.value)
    data = TemplateData(
        deploymentType=str(DeploymentType.REQUERIMIENTO.value),
        deploymentDate="04/11/2025",
        glpiTicketId=385,
        deploymentName="Agregar validación en trámites de cambio de sección y nivel de inglés",
        deploymentRequester="Erickson Gabriel Hinostroza Vargas",
        deploymentDeveloper="Alvaro Moises Castro Romero",
        deploymentApprover="Jainor Ruben Carbajal Parodi",
        deploymentDescription="""
                Agregar Validación en trámites de cambio de sección y nivel de inglés:

                ● Se agregó nueva validación al momento de solicitar trámite de cambio de sección y nivel de inglés en caso tenga un trámite activo.
                ● Consulta de datos a la nueva tabla de PEA_NOTAS

                """,
        flgTests="",
        flgRollback = "",
        flgDependencies = "X",
        components=[
            Component(
                type=str(ComponentType.PIPELINE.value),
                route="is-prod-cva-tramites-pipeline",
                repository="cva-tramites-backend",
                pullRequest="https://bitbucket.org/pe-innova-schools/cva-tramites-backend/pull-requests/328",
                observations="Ninguna"
            )
        ],
        scripts=[
            Script(
                order=1,
                name="script_1.sql",
                database="PEA",
                schema="PEA_NOTAS",
                type=ScriptType.DDL.value,
                description="Crear Tabla Nueva",
                validator="Jainor"
            )
        ],
        rollbackScripts=[
            RollbackScript(
                order=1,
                name="rollback_script_1.sql",
                database="PEA",
                schema="PEA_NOTAS",
                description="Se elimina tabla nueva"
            )
        ],
        steps=[
            Step(
                order=1,
                description="Subir archivo a S3",
                responsable="Fabricio Aguirre",
                action=None,
                result=None
            ),
            Step(
                order=2,
                description="Desplegar cambios de cva-tramites-backend",
                responsable="Fabricio Aguirre",
                action="Aprobar y merge el PR",
                result="Cambios desplegados correctamente"
            ),
            Step(
                order=3,
                description="Ejecución de Scripts",
                responsable="Fabricio Aguirre",
                action="Ejecutar Scripts indicadas",
                result="Consultas a la nueva tabla satisfactoriamente"
            ),
        ],
        rollbackPlans=[
            RollbackPlan(
                context="Los cambios de pipeline no se ven reflejados",
                action="Revisar errores y relanzar pipeline",
                responsable="Alvaro Castro",
                time="10 min"
            )
        ],
        verifications=[
            Verification(
                description="Validación de los cambios desplegados",
                result="La validación funciona correctamente",
                responsable="Alvaro Castro",
                status="Pendiente"
            )
        ],
        approvers=[
            Approver(
                role="Project Owner",
                name="Erickson Gabriel Hinostroza Vargas",
                date="04/11/2025"
            )
        ]
    )
    service = TemplateService()
    output_file = service.generate_deployment_doc(data)

    print(f"Documento generado en: {output_file}")
    #print(f"Documento generado")


if __name__ == "__main__":
    main()
