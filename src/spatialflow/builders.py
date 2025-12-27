"""
Workflow builder helpers for SpatialFlow SDK.

These functions help construct valid workflow payloads for common use cases.
"""

from typing import Dict, List, Literal, Optional

# Import models from generated package
from ._generated.spatialflow_generated.models import WorkflowIn

__all__ = [
    "build_geofence_webhook_workflow",
    "build_geofence_integration_workflow",
    "TriggerType",
]

TriggerType = Literal["geofence_enter", "geofence_exit", "geofence_dwell"]


def build_geofence_webhook_workflow(
    name: str,
    geofence_ids: List[str],
    webhook_url: str,
    *,
    trigger_type: TriggerType = "geofence_enter",
    description: Optional[str] = None,
    webhook_method: str = "POST",
    webhook_headers: Optional[Dict[str, str]] = None,
) -> WorkflowIn:
    """
    Build a workflow that triggers on geofence events and calls a webhook.

    This creates a simple two-node workflow: a geofence trigger connected to
    a webhook action. The workflow will fire whenever a device enters/exits
    any of the specified geofences.

    Args:
        name: Workflow name
        geofence_ids: List of geofence UUIDs to monitor
        webhook_url: URL to call when triggered
        trigger_type: "geofence_enter", "geofence_exit", or "geofence_dwell"
        description: Optional workflow description
        webhook_method: HTTP method (default: POST)
        webhook_headers: Optional HTTP headers

    Returns:
        WorkflowIn model ready for client.workflows.create()

    Example:
        >>> workflow_in = build_geofence_webhook_workflow(
        ...     name="Entry Alert",
        ...     geofence_ids=["uuid-1", "uuid-2"],
        ...     webhook_url="https://webhook.site/xxx",
        ... )
        >>> workflow = await client.workflows.create(workflow_in)
    """
    nodes = [
        {
            "id": "trigger-1",
            "type": "trigger",
            "position": {"x": 100, "y": 100},
            "data": {
                "label": f"Geofence {trigger_type.replace('_', ' ').title()}",
                "triggerType": trigger_type,
                "config": {
                    "type": trigger_type,
                    "geofence_ids": geofence_ids,
                },
            },
        },
        {
            "id": "action-1",
            "type": "action",
            "position": {"x": 400, "y": 100},
            "data": {
                "label": "Webhook",
                "actionType": "webhook",
                "config": {
                    "url": webhook_url,
                    "method": webhook_method,
                    "headers": webhook_headers or {"Content-Type": "application/json"},
                },
            },
        },
    ]

    edges = [{"id": "edge-1", "source": "trigger-1", "target": "action-1"}]

    return WorkflowIn(
        name=name,
        description=description,
        nodes=nodes,
        edges=edges,
    )


def build_geofence_integration_workflow(
    name: str,
    geofence_ids: List[str],
    integration_id: str,
    *,
    trigger_type: TriggerType = "geofence_enter",
    description: Optional[str] = None,
) -> WorkflowIn:
    """
    Build a workflow using a pre-configured integration.

    Use this when you've already created an integration (webhook, Slack, etc.)
    and want to reuse it across multiple workflows.

    Args:
        name: Workflow name
        geofence_ids: List of geofence UUIDs to monitor
        integration_id: ID of the integration to use as the action
        trigger_type: "geofence_enter", "geofence_exit", or "geofence_dwell"
        description: Optional workflow description

    Returns:
        WorkflowIn model ready for client.workflows.create()

    Example:
        >>> # First create an integration
        >>> integration = await client.integrations.create_webhook(
        ...     name="My Webhook",
        ...     url="https://webhook.site/xxx",
        ... )
        >>> # Then use it in a workflow
        >>> workflow_in = build_geofence_integration_workflow(
        ...     name="Entry Alert",
        ...     geofence_ids=["uuid-1"],
        ...     integration_id=integration.id,
        ... )
        >>> workflow = await client.workflows.create(workflow_in)
    """
    nodes = [
        {
            "id": "trigger-1",
            "type": "trigger",
            "position": {"x": 100, "y": 100},
            "data": {
                "label": f"Geofence {trigger_type.replace('_', ' ').title()}",
                "triggerType": trigger_type,
                "config": {
                    "type": trigger_type,
                    "geofence_ids": geofence_ids,
                },
            },
        },
        {
            "id": "action-1",
            "type": "action",
            "position": {"x": 400, "y": 100},
            "data": {
                "label": "Integration Action",
                "actionType": "integration",
                "config": {
                    "integration_id": integration_id,
                },
            },
        },
    ]

    edges = [{"id": "edge-1", "source": "trigger-1", "target": "action-1"}]

    return WorkflowIn(
        name=name,
        description=description,
        nodes=nodes,
        edges=edges,
    )
