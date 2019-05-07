from docutils import nodes
import sphinx
import hashlib
from sphinx.util.compat import Directive


class OroIntegrityCheck(Directive):
    """

    """
    required_arguments = 1
    has_content = True

    def run(self):
        document_hash = self.arguments[0]

        node = nodes.container()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)

        node_hash = self.calculate_hash(node.astext())

        env = self.state.document.settings.env
        if document_hash != node_hash:
            env.warn_node("Node hashes are different. %s expected, but %s given" % (node_hash, document_hash), node)
            warning_node = self.create_warning_node()
            return [warning_node, node]

        return [node]

    def calculate_hash(self, content):
        """
        Calculate hash of content
        :param content: str
        :return: str
        """

        sha1 = hashlib.sha1()
        sha1.update(content)
        return sha1.hexdigest()

    def create_warning_node(self):
        """
        Method creates warning node when hash of directive content
        is not match to content integrity hash in the rst document
        """

        item = nodes.paragraph()
        item.append(nodes.warning('', nodes.inline(text="This code example can be not actual for this version")))

        return item


def setup(app):
    app.add_directive('oro_integrity_check', OroIntegrityCheck)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
