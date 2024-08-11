from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime, timezone
from flask import url_for


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = db.paginate(query, page=page, per_page=per_page,
                                error_out=False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class Article(db.Model, PaginatedAPIMixin):
    __tablename__ = 'articles'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    created: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc))
    body: so.Mapped[str] = so.mapped_column(sa.String(200))
    tags: so.Mapped[str] = so.mapped_column(sa.String(100))

    def to_dict(self):
        data = {
            'id': self.id,
            'created': self.created,
            'body': self.body,
            'tags': [tag for tag in self.tags.split(';')],
            '_links': {
                'self': url_for('api.get_article', id=self.id),
            }
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'tags']:
            if field in data:
                setattr(self, field, data[field])
