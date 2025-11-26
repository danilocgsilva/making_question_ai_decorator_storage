"""alembic revision identifiers"""
revision = "001_initial"
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        "question_record",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("question", sa.Text, nullable=False),
        sa.Column("serialized_answer", sa.Text),
        sa.Column("result_answer", sa.Text),
        sa.Column("timestamp_start", sa.Float),
        sa.Column("timestamp_end", sa.Float),
        sa.Column("implementation_name", sa.String(255)),
        sa.Column("json_answer", sa.Text),
        sa.Column("json_parameters", sa.Text),
        sa.Column("json_hardware", sa.Text),
    )

def downgrade():
    op.drop_table("question_record")
