#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# revision identifiers, used by Alembic.
revision = 'f28f3f4494b3'
down_revision = '9c5c34dfd9f1'

from alembic import op
import iotronic.db.sqlalchemy.models
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'enabled_webservices',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('board_uuid', sa.String(length=36), nullable=True),
        sa.Column('http_port', sa.Integer(), nullable=True),
        sa.Column('https_port', sa.Integer(), nullable=True),
        sa.Column('dns', sa.String(length=100), nullable=True),
        sa.Column('zone', sa.String(length=100), nullable=True),
        sa.Column('extra',
                  iotronic.db.sqlalchemy.models.JSONEncodedDict(),
                  nullable=True),
        sa.ForeignKeyConstraint(['board_uuid'], ['boards.uuid'], ),
        sa.PrimaryKeyConstraint('id')
        )
    op.create_table(
        'webservices',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('port', sa.Integer(), nullable=True),
        sa.Column('name', sa.String(length=45), nullable=True),
        sa.Column('board_uuid', sa.String(length=36), nullable=True),
        sa.Column('secure', sa.Boolean(), nullable=True),
        sa.Column('extra',
                  iotronic.db.sqlalchemy.models.JSONEncodedDict(),
                  nullable=True),
        sa.ForeignKeyConstraint(['board_uuid'], ['boards.uuid'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid',
                            name='uniq_enabled_webservices0uuid'),
        sa.UniqueConstraint('port', 'board_uuid',
                            name='uniq_webservices_port_and_board'),
        sa.UniqueConstraint('board_uuid', 'port', 'name',
                            name='uniq_webservices_on_board')
        )